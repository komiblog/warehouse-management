<template>
    <div>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="8" style="min-height: 1px;"></el-col>
                    <el-col :span="10">
                        <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="input"> </el-input>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium">搜索</el-button>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium" @click="$router.push('/dashboard/newmail')">入库</el-button>
                    </el-col>
                    <el-col :span="2">
                        <el-button size="medium">所有记录</el-button>
                    </el-col>

                </el-row>
            </el-header>
            <el-main>
                <el-table :data="form.slice((currentPage - 1) * pageSize, currentPage * pageSize)" border
                    style="width: 100%" :header-cell-style="{ 'text-align': 'center' }"
                    :cell-style="{ 'text-align': 'center' }">
                    <el-table-column prop="userid" label="产品ID" width="100"> </el-table-column>
                    <el-table-column prop="name" label="名称" width="150"> </el-table-column>
                    <el-table-column prop="sex" label="类别" width="150"> </el-table-column>
                    <el-table-column prop="phone" label="数量" width="100"> </el-table-column>
                    <el-table-column prop="email" label="价格" width="100"> </el-table-column>
                    <el-table-column prop="department" label="描述" width="300">
                    </el-table-column>
                    <!-- <el-table-column prop="postalcode" label="地区" width="260">
      </el-table-column> -->
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button size="medium">出库</el-button>
                            <el-button size="medium">修改</el-button>
                            <el-button size="medium" type="danger">删除</el-button>
                            <el-button size="medium">日志</el-button>

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
            currentPage: 1, // 当前页码
            pageSize: 5, // 每页的数据条数
        };
    },
    created: function () {
        this.$http.get("/profile/showAll").then((res) => {
            console.log(res.data);
            let r = res.data;
            for (let i = r.length - 1; i > -1; i--) {
                r[i].sex = r[i].sex === 0 ? "未知" : r[i].sex === 1 ? "男" : "女";
            }
            this.form = r;
        });
    },

    methods: {
        editdata(row) {
            this.$router.push({
                path: "/dashboard/changeinfo",
                query: {
                    userid: row.userid,
                    phone: row.phone,
                    email: row.email,
                    name: row.name,
                },
            });
        },

        handleDelete(row) {
            this.$http({
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                method: "post",
                url: "profile/del",
                data: "id=" + row.userid,
            })
                .then((res) => {
                    if (res.data.code === 1) {
                        this.$alert("成功删除" + row.name + "的信息", "删除成功");

                        this.$http.get("/profile/showAll").then((res) => {
                            let r = res.data;
                            for (let i = r.length - 1; i > -1; i--) {
                                r[i].sex =
                                    r[i].sex === 0 ? "未知" : r[i].sex === 1 ? "男" : "女";
                            }
                            this.form = r;
                        });
                    } else if (res.data.code === 0) {
                        this.$alert("未能删除" + row.name + "的信息", "删除失败");
                    }
                })
                .catch((err) => {
                    console.log(err);
                    this.$alert("请重试", "请求失败");
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