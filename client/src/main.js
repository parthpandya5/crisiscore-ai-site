import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import BootstrapVue3 from 'bootstrap-vue-3';
import 'bootstrap/dist/css/bootstrap.css';
import './styles/theme.scss';

import { DefaultApolloClient } from '@vue/apollo-composable';
import { apolloClient } from './apollo/client';

const app = createApp(App);
app.use(router);
app.use(BootstrapVue3);
app.provide(DefaultApolloClient, apolloClient);
app.mount('#app');
