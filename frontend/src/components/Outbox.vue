<template>
  <div>
    <el-table
      :data="form.slice((currentPage - 1) * pageSize, currentPage * pageSize)"
      border
      style="width: 100%"
      :header-cell-style="{ 'text-align': 'center' }"
      :cell-style="{ 'text-align': 'center' }"
    >
      <el-table-column prop="id" label="编号" width="60"> </el-table-column>
      <el-table-column prop="name" label="收件人" width="80"> </el-table-column>
      <el-table-column prop="time" label="时间" width="120"> </el-table-column>
      <el-table-column prop="title" label="标题" width="200"> </el-table-column>
      <el-table-column prop="content" label="内容" width="380">
      </el-table-column>
      <el-table-column prop="attachmen" label="附件" width="100">
        <template slot-scope="scope">
          <el-button size="medium" @click="download(scope.row)">下载</el-button>
        </template>
      </el-table-column>
      <el-table-column prop="readflag" label="阅读状态" width="80">
        <template slot-scope="scope">
          {{ scope.row.readflag ? "已读" : "未读" }}</template
        >
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="medium" @click="detailed(scope.$index, scope.row)"
            >详细</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页器 -->
    <div class="block" style="margin-top: 15px">
      <el-pagination
        align="center"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[1, 5, 10, 20]"
        :page-size="pageSize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="form.length"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  created: function () {
    let that = this;
    let getNameById = async function (id) {
      let resp;
      await that.$http.get("/profile/show?userid=" + id).then((res) => {
        resp = res;
      });
      return resp;
    };
    this.$http.get("/mail/sendlist").then(async (res) => {
      let r = res.data;
      for (let i = r.length - 1; i > -1; i--) {
        let toid = r[i].toid;
        let p = await getNameById(toid);
        r[i].name = p.data[0].name;
        console.log(r[i].name);
      }
      this.form = r;
    });
  },
  data() {
    return {
      form: [],
      currentPage: 1, // 当前页码
      pageSize: 5, // 每页的数据条数
    };
  },
  methods: {
    detailed(index, row) {
      this.$router.push({
        path: "/dashboard/detailmail",
        query: {
          name: row.name,
          time: row.time,
          title: row.title,
          content: row.content,
          read: "收件人",
          attachment: row.attachment,
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