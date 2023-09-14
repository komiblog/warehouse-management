<template>
    <div class="homeWrap">
        <el-container style="height: 100%; border: 1px solid #eee">
            <!-- <el-aside width="200px">
        <el-menu
          :default-openeds="['1', '3']"
          style="min-height: 100%; overflow-x: hidden; text-align: left"
          background-color="rgb(48,65,86)"
          text-color="#fff"
          router
        >
          <div style="height=60px ;line-height: 60px; text-align: center">
            <b style="color: white">企业信息管理系统</b>
          </div>
          <el-submenu index="1">
            <template slot="title"
              ><i class="el-icon-message"></i>通讯管理</template
            >
            <el-submenu index="1-1">
              <template slot="title">通讯录管理</template>
              <el-menu-item index="/dashboard/addressbook"
                >查看通讯录</el-menu-item
              >
              <el-menu-item index="/dashboard/newman">新增联系人</el-menu-item>
            </el-submenu>
            <el-submenu index="1-2">
              <template slot="title">邮件管理</template>
              <el-menu-item index="/dashboard/inbox">收件箱</el-menu-item>
              <el-menu-item index="/dashboard/outbox">发件箱</el-menu-item>
              <el-menu-item index="/dashboard/newmail">新增邮件</el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"
              ><i class="el-icon-menu"></i>个人管理</template
            >

            <el-menu-item index="/dashboard/personalinfo"
              >个人信息查询</el-menu-item
            >
            <el-menu-item index="/dashboard/changeheadshot"
              >头像编辑</el-menu-item
            >
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"
              ><i class="el-icon-setting"></i>企业管理</template
            >
            <el-menu-item index="3-1">公司公告</el-menu-item>
            <el-menu-item index="3-2">工作会议</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside> -->

            <el-container>
                <!-- <el-header style="text-align: right; font-size: 12px">
          <el-dropdown v-model="name">
            <span>{{ name }} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="$router.push('/dashboard')"
                >返回首页</el-dropdown-item
              >
              <el-dropdown-item @click.native="logout"
                >退出登录</el-dropdown-item
              >
            </el-dropdown-menu>
          </el-dropdown>
        </el-header> -->

                <el-main>
                    <!--声明路由链接-->
                    <router-link to="/dashboard/product"></router-link>
                    <router-link to="/dashboard/changinfo"></router-link>
                    <router-link to="/dashboard/inbox"></router-link>
                    <router-link to="/dashboard/outbook"></router-link>
                    <router-link to="/dashboard/newmail"></router-link>
                    <router-link to="/dashboard/personalinfo"></router-link>
                    <!--声明路由占位符标签-->
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>



<script>
export default {
    components: {},
    name: "Dashboard",
    data() {
        return {
            name: "王小晖",
        };
    },
    created: function () {
        this.$http.get("profile/show").then((res) => {
            this.name = res.data[0].name;
        });
    },
    methods: {
        logout() {
            this.$http
                .get("/logout")
                .then((res) => {
                    if (res.data.code === 1) {
                        this.$message.success("退出登录成功");
                        this.$router.push("/login");
                    }
                })
                .catch((err) => {
                    this.$message.warning("退出登录失败");
                    console.log(err);
                });
        },
    },
};
</script>


<style>
.el-header {
    background-color: #edf5fd;
    color: rgb(31, 36, 41);
    line-height: 60px;
}

.el-aside {
    color: #333;
    box-shadow: 2px 0 6px rgb(125, 133, 141);
}

/* 去除滚动条 */
.el-aside::-webkit-scrollbar {
    display: none;
}

.homeWrap {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>
