<template>
    <div>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="2">
                        <el-button size="medium" @click="$router.push('/dashboard/product')">返回</el-button>
                    </el-col>

                </el-row>
            </el-header>
            <el-main>
                <el-row>
                    <el-col :span="6" style="min-height: 1px;"></el-col>
                    <el-col :span="12">
                        <el-table :data="form.slice((currentPage - 1) * pageSize, currentPage * pageSize)" border
                            style="width: 100%" :header-cell-style="{ 'text-align': 'center' }"
                            :cell-style="{ 'text-align': 'center' }">
                            <el-table-column prop="r_id" label="记录ID" width="70"> </el-table-column>
                            <el-table-column prop="p_name" label="名称" width="150"> </el-table-column>
                            <el-table-column prop="u_name" label="用户" width="100"> </el-table-column>
                            <el-table-column prop="r_num" label="数量" width="100"> </el-table-column>
                            <el-table-column prop="type" label="操作" width="75"> </el-table-column>
                            <el-table-column prop="r_time" label="时间"> </el-table-column>
                        </el-table>
                        <!-- 分页器 -->
                        <div class="block" style="margin-top: 15px">
                            <el-pagination align="center" @size-change="handleSizeChange"
                                @current-change="handleCurrentChange" :current-page="currentPage"
                                :page-sizes="[1, 5, 10, 20]" :page-size="pageSize"
                                layout="total, sizes, prev, pager, next, jumper" :total="form.length">
                            </el-pagination>
                        </div>
                    </el-col>
                    <el-col :span="6" style="min-height: 1px;"></el-col>
                </el-row>
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
        let url = "";
        if (this.$route.query.p_id === undefined) {
            url = "/record/record";
        } else {
            url = "/record/record/" + this.$route.query.p_id;
        }
        this.$http.get(url).then((res) => {
            console.log(res.data);
            this.form = res.data;
        });
    },

    methods: {

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