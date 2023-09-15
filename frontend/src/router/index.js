import VueRouter from "vue-router";
import Vue from "vue";
// 导入组件
import Dashboard from "@/views/Dashboard.vue";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";
// 子组件
import Product from "@/components/Product.vue";
import Inbox from "@/components/Inbox.vue";
import Outbox from "@/components/Outbox.vue"
import Input from "@/components/Input.vue";
import Output from "@/components/Output.vue";
import Record from "@/components/Record.vue";
import Update from "@/components/Update.vue";
import ChangeHeadshot from "@/components/ChangeHeadshot.vue";
import PersonalInfo from "@/components/PersonalInfo.vue";
import ChangeInfo from "@/components/ChangeInfo.vue"
import NewMan from "@/components/NewMan.vue"
import DetailMail from "@/components/DetailMail.vue"


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
                { path: 'inbox', component: Inbox },
                { path: 'outbox', component: Outbox },
                { path: 'input', component: Input },
                { path: 'changeheadshot', component: ChangeHeadshot },
                { path: 'personalinfo', component: PersonalInfo },
                { path: 'changeinfo', component: ChangeInfo },
                { path: 'newman', component: NewMan },
                { path: 'detailmail', component: DetailMail },
            ]
        },
        { path: '/login', component: Login },
        { path: '/signup', component: Signup },
        { path: '/', redirect: "/dashboard" },
    ]
})



// 注册一个全局前置守卫
// router.beforeEach((to, from, next) => {
//     if (to.path !== '/login' && to.path !== '/signup') {    //判断当前路由是否需要进行权限控制
//         axios.get("status").then((res) => {
//             if (res.data.code == '1') {
//                 next()
//             } else {
//                 next({
//                     path: "/login"
//                 })
//             }
//         })
//     } else {
//         next() // 放行
//     }
// })


export default router