import{r,o as n,w as u,a as d,c,d as p,b as i}from"./index.S7RG_dfA.js";import{b as f}from"./index.Zkar--a9.js";/* empty css                        */import{_ as m}from"./_plugin-vue_export-helper.x3n3nnut.js";import"./index.5btRwMe0.js";const v={props:{url:{type:String},delay:{type:Boolean,default:!1}},components:{},setup(o){const e=r(null),t=r(!1),l=f(e);return n(()=>{if(!(document.documentElement.dataset.speed>2)){for(var s in e.value.children){var a=e.value.children[s];typeof a.tagName=="string"&&a.tagName==="SOURCE"&&(a.src=a.dataset.src)}o.delay?setTimeout(()=>{e.value.load(),e.value.classList.remove("lazy"),t.value=!0},1500):(e.value.load(),e.value.classList.remove("lazy"),t.value=!0)}}),u(l,s=>{s?t.value&&e.value.play():t.value&&e.value.pause()},{immediate:!0}),{video:e,isVisible:l}}},_={class:"video-inline z-0 transition-transform duration-[1.5s] group-hover:scale-110"},y={ref:"video",class:"lazy noise pointer-events-none left-0 top-0 z-20 block h-full w-full",autoplay:"",muted:"",loop:"",playsinline:"",preload:"true",width:"610",height:"254"},h=["data-src"];function g(o,e,t,l,s,a){return d(),c("div",_,[p(o.$slots,"default"),i("video",y,[i("source",{"data-src":t.url,type:"video/mp4"},null,8,h)],512)])}const V=m(v,[["render",g]]);export{V as default};
