<template>
    <div>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="2">
                        <el-button size="medium" @click="logout">注销</el-button>
                    </el-col>
                    <el-col :span="6" style="min-height: 1px;"></el-col>
                    <el-col :span="10">
                        <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="inputany"> </el-input>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium" @click="search">搜索</el-button>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium" @click="$router.push('/dashboard/input')">入库</el-button>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium" @click="$router.push('/dashboard/record')">所有记录</el-button>
                    </el-col>

                </el-row>
            </el-header>
            <el-main>
                <el-table :data="form.slice((currentPage - 1) * pageSize, currentPage * pageSize)" border
                    style="width: 100%" :header-cell-style="{ 'text-align': 'center' }"
                    :cell-style="{ 'text-align': 'center' }">
                    <el-table-column prop="p_id" label="产品ID" width="70"> </el-table-column>
                    <el-table-column prop="p_name" label="名称" width="150"> </el-table-column>
                    <el-table-column prop="p_type" label="类别" width="100"> </el-table-column>
                    <el-table-column prop="p_count" label="数量" width="100"> </el-table-column>
                    <el-table-column prop="p_price" label="价格" width="100"> </el-table-column>
                    <el-table-column prop="p_depiction" label="描述" width="350">
                    </el-table-column>
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button size="medium" @click="reduce(scope.row)">出库</el-button>
                            <el-button size="medium" @click="update(scope.row)">修改</el-button>
                            <el-button size="medium" type="danger" @click="deleterow(scope.row)">删除</el-button>
                            <el-button size="medium" @click="record(scope.row)">记录</el-button>

                        </template>
                    </el-table-column>
                </el-table>
                <!-- 分页器 -->
                <div class="block" style="margin-top: 15px">
                    <el-pagination align="center" @size-change="handleSizeChange" @current-change="handleCurrentChange"
                        :current-page="currentPage" :page-sizes="[1, 5, 10, 20]" :page-size="pageSize"
                        layout="total, sizes, prev, pager, next, jumper" :total="form.length">
                    </el-pagination>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: [],
            inputany: "",
            currentPage: 1, // 当前页码
            pageSize: 5, // 每页的数据条数
        };
    },
    created: function () {
        this.$http.get("/manage/product").then((res) => {
            console.log(res.data);
            this.form = res.data;
        });
    },

    methods: {
        record(row) {
            this.$router.push({
                path: "/dashboard/record",
                query: {
                    p_id: row.p_id
                },
            })
        },
        deleterow(row) {
            this.$confirm('确定删除?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.$http
                    .delete("/manage/product/" + row.p_id)
                    .then((res) => {
                        if (res.status === 200) {
                            // 刷新页面
                            this.$http.get("/manage/product").then((res) => {
                                console.log(res.data);
                                this.form = res.data;
                            });
                            this.$message.success(res.data.message);
                        }
                    })
                    .catch((err) => {
                        console.log(err);
                        this.$message.warning(err.response.data.message);
                    });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            })
        },
        search() {
            this.$http
                .get("/manage/search/" + this.inputany)
                .then((res) => {
                    if (res.status === 200) {
                        this.form = res.data;
                        this.$message.success("查询成功");
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.$message.warning("查询失败");
                });
        },
        logout() {
            this.$http
                .get("/auth/logout")
                .then((res) => {
                    if (res.status === 200) {
                        this.$message.success(res.data.message);
                        this.$router.push("/login");
                    }
                })
                .catch((err) => {
                    this.$message.warning("退出登录失败");
                    console.log(err);
                });
        },

        reduce(row) {
            this.$router.push({
                path: "/dashboard/output",
                query: {
                    p_id: row.p_id,
                    p_name: row.p_name
                },
            })

        },
        update(row) {
            this.$router.push({
                path: "/dashboard/update",
                query: {
                    p_id: row.p_id,
                    p_name: row.p_name,
                    p_type: row.p_type,
                    p_price: row.p_price,
                    p_depiction: row.p_depiction,
                },
            });
        },


        //每页条数改变时触发 选择一页显示多少行
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
            this.currentPage = 1;
            this.pageSize = val;
        },
        //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
            this.currentPage = val;
        },
    },
};
</script>