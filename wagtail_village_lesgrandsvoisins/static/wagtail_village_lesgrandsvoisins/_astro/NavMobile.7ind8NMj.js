import{r as m,o as v,a as c,c as d,b as o,u as _,m as k,h as w,T as g,j as b,v as x,d as p,F as y,s as M,A as S,t as C}from"./index.S7RG_dfA.js";import{c as f}from"./index.Zkar--a9.js";/* empty css                        */import{_ as L}from"./_plugin-vue_export-helper.x3n3nnut.js";import"./index.5btRwMe0.js";const B={__name:"NavMobile",props:{translations:Object,menu:Array,active:String},setup(i,{expose:r}){r();const t=m(!1),e=m(null),a=i,h=()=>{t.value=!t.value,n.value=t.value},s=l=>{if(a.active===""&&l=="/"||a.active!==""&&l.startsWith(`/${a.active}`))return!0};let n;v(()=>{e.value=document.getElementsByTagName("body")[0],n=f(e.value)});const u={show:t,body:e,props:a,toggleMenu:h,isActive:s,get isLocked(){return n},set isLocked(l){n=l},ref:m,onMounted:v,get useScrollLock(){return f}};return Object.defineProperty(u,"__isScriptSetup",{enumerable:!1,value:!0}),u}},F={class:"contents"},N=["aria-label"],A=o("path",{id:"line_x5F_3",d:"M4.88 50H96.4",stroke:"currentColor","stroke-width":"12","stroke-linecap":"round","stroke-miterlimit":"10"},null,-1),j=o("path",{id:"line_x5F_2",d:"M4.88 50H96.4",stroke:"currentColor","stroke-width":"12","stroke-linecap":"round","stroke-miterlimit":"10"},null,-1),H=o("path",{id:"line_x5F_1",d:"M4.88 50H96.4",stroke:"currentColor","stroke-width":"12","stroke-linecap":"round","stroke-miterlimit":"10"},null,-1),T=[A,j,H],z={class:"surface-base nav-mobile fixed inset-0 grid h-full auto-rows-min place-items-center gap-4 px-4 pt-4"},D={href:"/",class:"mx-auto max-w-[12rem] pt-10"},E={class:"mobile-links mt-3 w-full text-center",slot:"links"},O=["href"];function V(i,r,t,e,a,h){return c(),d("span",F,[o("button",{"aria-label":e.show?t.translations.close:t.translations.menu,onClick:r[0]||(r[0]=s=>e.toggleMenu()),class:_(`nav-mobile-btn relative ml-auto flex md:hidden ${e.show?"text-primary":""}`)},[(c(),d("svg",{xmlns:"http://www.w3.org/2000/svg","xml:space":"preserve",class:_(["menu-icon h-6 w-6",e.show?"close":"menu"]),style:{"enable-background":"new 0 0 100 100"},version:"1.1",viewBox:"0 0 100 100"},T,2))],10,N),k(g,{name:"nested"},{default:w(()=>[b(o("div",z,[o("a",D,[p(i.$slots,"logo")]),o("div",E,[(c(!0),d(y,null,M(t.menu,(s,n)=>(c(),d("a",{href:s.href,onClick:r[1]||(r[1]=u=>e.toggleMenu()),key:s.href,style:S(`--animation-delay: ${(n+1)*100}ms`),class:_(`title-md inner block w-full py-3 font-light transition-all duration-300 hover:text-primary ${e.isActive(s.href)?"active text-primary":""}`)},C(s.label),15,O))),128))]),p(i.$slots,"social")],512),[[x,e.show]])]),_:3})])}const I=L(B,[["render",V]]);export{I as default};
