import Vue from 'vue'
import App from './App.vue'
// 导入element-ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 导入第三方图标库
import 'font-awesome/css/font-awesome.min.css'
// 导入http轻量库axios
import axios from 'axios'
// 导入路由
import router from "@/router";


// 配置axios默认域名
axios.defaults.baseURL = "http://localhost:8088"
// 前端cookie请求
axios.defaults.withCredentials = true
// 自定义vue属性http
Vue.prototype.$http = axios


Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router: router,
}).$mount('#app')
