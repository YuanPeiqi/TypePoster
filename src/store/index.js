import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
// import poster from './modules/poster/poster'
import logger from 'vuex/dist/logger'

Vue.use(Vuex)

const store = new Vuex.Store({
    // modules: {
    //   poster
    // },
    state: {
        pickerOptions: {
            disabledDate(time) {
                return time.getTime() < Date.now()
            },
            shortcuts: [{
                text: '今天',
                onClick(picker) {
                    picker.$emit('pick', new Date())
                }
            }, {
                text: '明天',
                onClick(picker) {
                    const date = new Date()
                    date.setTime(date.getTime() + 3600 * 1000 * 24)
                    picker.$emit('pick', date)
                }
            }, {
                text: '一周后',
                onClick(picker) {
                    const date = new Date()
                    date.setTime(date.getTime() + 3600 * 1000 * 24 * 7)
                    picker.$emit('pick', date)
                }
            }]
        },
        info_form: [],
        poster_list: [],
        blending_list: [],
        first_render: false
    },
    mutations: {
        setPosterList(state, value) {
            state.poster_list = value
            console.log(state.poster_list)
        },
        setBlendingList(state, value) {
            state.blending_list = value
        }
    },
    actions: {
        setPosterList(context) {
            context.commit('setPosterList')
        },
        setBlendingList(context) {
            context.commit('setBlendingList')
        }
    },
    getters,
    plugins: process.env.NODE_ENV !== 'production' ? [logger()] : []
})

export default store
