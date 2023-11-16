import VueRouter from "vue-router";
import Vue from "vue";
// 导入组件
import Dashboard from "@/views/Dashboard.vue";
import Login from "@/views/Login.vue";
// 子组件
import Product from "@/components/Product.vue";
import Input from "@/components/Input.vue";
import Output from "@/components/Output.vue";
import Record from "@/components/Record.vue";
import Update from "@/components/Update.vue";


import axios from "axios";
// 将VueRouter设置为Vue的插件
Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        {
            path: '/dashboard', component: Dashboard, children: [
                { path: '', redirect: 'product' },  // 重定向
                { path: 'output', component: Output },
                { path: 'product', component: Product },
                { path: 'update', component: Update },
                { path: 'record', component: Record },
                { path: 'input', component: Input },
            ]
        },
        { path: '/login', component: Login },
        { path: '/', redirect: "/dashboard" },
    ]
})




// 定义要发送的数据
const postData = {
    u_name: '1',
    u_pwd: '1'
};
注册一个全局前置守卫
router.beforeEach((to, from, next) => {
    if (to.path !== '/login') {    //判断当前路由是否需要进行权限控制
        axios.post("/auth/login", postData).then((res) => {
            if (res.status === 200) {
                console.log("权限通过")
                next()
            }
        }).catch((err) => {
            console.log(err)
            console.log("权限不通过")
            next({
                path: "/login"
            })
        })
    } else {
        next() // 放行
    }
})


export default router