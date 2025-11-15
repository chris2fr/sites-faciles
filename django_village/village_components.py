from django.templatetags.static import static

from django_village.utils import lorem_ipsum


# Sample SVG file
# with open("django_village/static/img/gouvernement.svg") as svg_file:
#     gov_svg = svg_file.read()
gov_svg = '<svg version="1.1" role="img" aria-label=”Gouvernement” xmlns="http://www.w3.org/2000/svg"xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 895 455" xml:space="preserve"><style type="text/css">.st0 {fill: #1F356C;}.st1 {fill: #000091;}.st2 {fill: #E1000F;}.st3 {fill: #808080;}</style><rect fill="#ffffff" width="895" height="455"></rect><g><g><g><path d="M61.4,206.5v-12.2H43v-13.3h33v30.7c-6.7,9-17.9,14.7-31.4,14.7c-23.4,0-39.4-17.5-39.4-38.1c0-20.6,15.6-38.1,38.4-38.1c13.1,0,23.8,5.9,30.4,14.6l-11.5,9c-4.1-5.9-10.6-9.9-18.9-9.9c-13.6,0-23.3,10.6-23.3,24.4s10.2,24.4,24.3,24.4C51.4,212.8,57.3,210.5,61.4,206.5z" /><path d="M162.8,188.4c0,20.6-15.6,38.1-38.3,38.1c-22.8,0-38.4-17.5-38.4-38.1c0-20.6,15.6-38.1,38.4-38.1C147.3,150.3,162.8,167.8,162.8,188.4z M147.8,188.4c0-13.8-9.7-24.4-23.2-24.4c-13.6,0-23.3,10.6-23.3,24.4s9.7,24.4,23.3,24.4C138.1,212.8,147.8,202.2,147.8,188.4z" /><path d="M218.7,152.3h14.6v43.9c0,19-11.1,30.3-29.3,30.3c-18,0-29.2-11.3-29.2-30.3v-43.9h14.6v45.2c0,9.7,5.5,15.4,14.6,15.4c9,0,14.5-5.7,14.5-15.4V152.3z" /><path d="M258.1,152.3l21.3,56.4l21.3-56.4h15.6L289,224.5h-19.2l-27.3-72.2H258.1z" /><path d="M327.6,152.3h42.1v12.5h-27.4v16.7h23.3V194h-23.3v18h27.4v12.5h-42.1V152.3z" /><path d="M386.8,152.3h22.1c15.9,0,25.7,8.1,25.7,21.5c0,8.7-4.2,15.2-11.5,18.7l22.7,32h-17.5l-19.2-29.2h-7.5v29.2h-14.6V152.3zM401.4,164.8v18h8.2c6.2,0,9.8-3.3,9.8-9.2c0-5.5-3.6-8.9-9.8-8.9H401.4z" /><path d="M454.8,152.3h18.8l32.3,51.7v-51.7h14.6v72.2h-18.8l-32.3-51.9v51.9h-14.6V152.3z" /><path d="M540.8,152.3h42.1v12.5h-27.4v16.7h23.3V194h-23.3v18h27.4v12.5h-42.1V152.3z" /><pathd="M600,152.3h18.5l17.4,29.7l17.4-29.7h18.5v72.2h-14.6v-51.3L641,199.7h-10.3l-16.1-26.6v51.3H600V152.3z" /><path d="M692,152.3H734v12.5h-27.4v16.7h23.3V194h-23.3v18H734v12.5H692V152.3z" /><path d="M751.1,152.3h18.8l32.3,51.7v-51.7h14.6v72.2H798l-32.3-51.9v51.9h-14.6V152.3z" /><path d="M829.7,152.3h59.2v13.3h-22.3v58.9H852v-58.9h-22.3V152.3z" /></g></g><g><path class="st0" d="M100.5,89.9C100.6,89.9,100.6,89.9,100.5,89.9c0.4-0.2,0.6-0.3,0.8-0.5c0,0-0.1,0-0.1,0C101,89.5,100.8,89.7,100.5,89.9" /><path class="st0" d="M137.2,77.7l-0.2,0.2C137.1,77.9,137.2,77.8,137.2,77.7" /><path class="st1" d="M125.6,90.5c1.1-1.1,2.2-2.2,3.2-3.4h0c2-2.3,4-4.4,6.3-6.4c0.7-0.6,1.4-1.2,2.1-1.6c0.2-0.2,0.2-0.6,0.4-0.8c-0.9,0.4-1.5,1.1-2.5,1.5c-0.2,0-0.4-0.2-0.2-0.4c0.7-0.5,1.4-1,2-1.5c0,0-0.1,0-0.1,0c-0.2,0-0.2-0.2-0.2-0.4c-2.5-0.4-4.3,1.3-6,2.8c-0.4,0.2-0.8-0.2-0.9-0.2c-2.8,0.9-4.9,3.4-7.7,4.5v-0.4c-1.1,0.4-2.2,1.1-3.4,1.3c-1.7,0.4-3.2,0.2-4.7,0.2c-2.3,0.2-4.6,0.7-6.9,1.2c-0.1,0-0.1,0-0.2,0.1c-1.2,0.3-2.4,0.8-3.5,1.4l-0.1,0.1c-0.1,0.1-0.2,0.2-0.3,0.3c-0.4,0.4-0.8,0.9-1.3,1.1c-1.2,0.6-2.1,1.6-3.1,2.5c-0.1,0.1-0.2,0.1-0.3,0.1c-1,1-2,2-3,2.9c-0.1,0.1-0.4,0.1-0.6,0.1c0,0,0,0,0,0c0-0.1,0.1-0.1,0.1-0.2c0.2-0.3,0.3-0.5,0.5-0.8c0.2-0.3,0.4-0.6,0.6-0.9c0.3-0.4,0.5-0.8,0.8-1.1c0.1-0.1,0.1-0.2,0-0.2c-0.1-0.1-0.2-0.1-0.3-0.1c0.9-0.9,2.1-1.7,3.2-2.4v0c-0.1,0-0.3-0.1-0.2-0.2c0.1-0.2,0.2-0.3,0.3-0.5c0-0.1,0-0.1,0.1-0.2c0-0.1-0.1-0.1-0.1-0.2c-0.3,0.2-0.6,0.4-0.9,0.6c-0.5,0.4-0.8,1.2-1.5,1.2c0,0-0.2,0-0.3,0c-0.1,0-0.2,0-0.2-0.1c0,0,0,0,0,0c0,0,0,0,0-0.1c0,0,0,0,0,0c0-0.1,0.1-0.1,0.1-0.2c0-0.1,0.1-0.1,0.1-0.2c0,0,0-0.1,0.1-0.1c0-0.1,0.1-0.2,0.1-0.2c0-0.1,0.1-0.1,0.1-0.2c0.1-0.1,0.2-0.3,0.2-0.4c0-0.1,0.1-0.1,0.1-0.2c0.1-0.1,0.1-0.2,0.2-0.3c0.1-0.2,0-0.3-0.1-0.3c0.3-0.5,0.8-0.8,1.3-1.1h-0.1c0.7-0.4,1.5-0.8,2.2-1.2c0.1-0.1,0.2-0.2,0.3-0.3c-1.1,0.4-2,0.9-3,1.5c0,0-0.2,0.1-0.3,0.2c0,0-0.2,0.1-0.5-0.2c0,0,0-0.1,0-0.1c0.2-0.4,0.8-0.6,1.1-0.9c0.2,0,0.4,0,0.4,0.2c6.1-4.7,14.4-3.6,21.4-6c0.6-0.4,1.1-0.8,1.7-1.1c0.9-0.4,1.7-1.3,2.8-1.9c1.5-1.1,2.6-2.5,3.2-4.3c0-0.2-0.2-0.4-0.2-0.4c-2.5,2.6-5.3,4.7-8.3,6.2c-4,2.1-8.3,1.7-12.5,2.3c0.2-0.4,0.6-0.4,0.9-0.4c0-0.6,0.4-0.8,0.8-1.1h0.6c0.2,0,0.2-0.4,0.4-0.4c0.4,0,1-0.2,0.8-0.2c-0.6-0.8-1.7,0.6-2.6,0c0.4-0.4,0.2-0.9,0.6-1.1h0.8c0-0.4,0.4-0.8,0.4-0.8c2.8-1.7,5.5-3,8.1-4.5c-0.6,0-0.9,0.6-1.5,0.2c0.4,0,0-0.6,0.4-0.6c2.1-0.6,3.8-1.7,5.9-2.5c-0.8,0-1.3,0.6-2.1,0c0.4-0.2,0.6-0.6,1.1-0.6v-0.6c0-0.2,0.2-0.2,0.4-0.2c-0.2,0-0.4-0.2-0.4-0.2c0.2-0.4,0.8-0.2,1.1-0.6c-0.2,0-0.6,0-0.6-0.2c0.6-0.8,1.5-0.9,2.5-1.1c-0.2-0.4-0.8,0-0.8-0.4c0-0.2,0.2-0.2,0.4-0.2h-0.4c-0.4-0.2-0.2-0.6-0.2-0.8c1.1-1.3,1.1-3,1.7-4.5c-0.2,0-0.4,0-0.4-0.2c-1.9,2.1-4.9,2.8-7.7,3.6H116c-0.9,0.4-2.3,0.4-3.2-0.2c-0.8-0.4-1.1-0.9-1.9-1.5c-1.5-0.9-3-1.7-4.7-2.3c-4.7-1.5-9.6-2.3-14.5-2.1c2.1-1.1,4.4-1.2,6.6-1.9c3.2-0.9,6.2-2.1,9.6-1.9c-0.6-0.2-1.3,0-1.9,0c-2.6-0.2-5.3,0.6-8.1,1.1c-1.9,0.4-3.6,1.1-5.5,1.5c-1.1,0.4-1.7,1.5-3,1.3v-0.6c1.9-2.3,4.2-4.5,7.2-4.7c3.4-0.6,6.6,0,10,0.4c2.5,0.2,4.7,0.8,7.2,1.3c0.9,0,1.1,1.5,1.9,1.7c1.1,0.4,2.3,0,3.4,0.8c0-0.4-0.2-0.8,0-1.1c0.8-0.8,1.7,0.2,2.5-0.2c1.5-0.9-1.3-2.6-2.1-4c0-0.2,0.2-0.4,0.2-0.4c1.5,1.3,2.6,2.8,4.5,3.8c0.9,0.4,3.2,0.9,2.8-0.2c-0.9-2.1-2.8-3.8-4.4-5.7v-0.8c-0.4,0-0.4-0.2-0.6-0.4v-0.8c-0.8-0.4-0.6-1.1-0.9-1.7c-0.6-0.9-0.2-2.3-0.6-3.4c-0.4-1.1-0.6-2.1-0.8-3.2c-0.6-3.2-1.3-6-1.7-9.1c-0.4-3.6,2.1-6.4,3.8-9.6c1.3-2.3,2.8-4.5,5.3-6c0.6-2.3,2.1-4.2,3.6-6c1.5-1.8,4-3,5.8-3.8c2.6-1.2,5-1.9,5-1.9H11.1v100h92.7c3.6-2.6,7.2-3.8,12.2-6.3C118.4,94.8,123.8,92.3,125.6,90.5 M96.6,76.9c-0.4,0-1.1,0.2-0.9-0.2c0.2-0.9,1.5-0.9,2.3-1.3c0.4-0.2,0.9-0.6,1.3-0.4c0.4,0.6,0.9,0.4,1.3,0.8C99.4,76.9,97.9,76.4,96.6,76.9 M67.6,72.8c0,0-0.2-0.2-0.2-0.4c2.5-3.2,4.3-6.2,6.1-9.6c2.5-1.3,4.5-3.2,6.4-5.3c3.2-3.4,6.6-6.4,10.6-8.3c1.5-0.6,3.4-0.4,4.9,0.2c-0.6,0.8-1.5,0.6-2.3,1.1c-0.2,0-0.4,0-0.6-0.2c0.2-0.2,0.2-0.4,0.2-0.6c-1.9,2.1-4.5,3-6,5.5c-1.1,1.9-1.9,4.3-4.3,4.9c-0.8,0.2,0.2-0.6-0.2-0.4C76.3,63.3,72.2,67.7,67.6,72.8 M83.3,60.3c-0.2,0.4-0.4,0.4-0.6,0.8c-0.2,0.4-0.4,0.6-0.8,0.8c-0.2,0-0.4,0-0.4-0.2c0.2-0.8,0.8-1.5,1.5-1.7C83.3,59.9,83.3,60.1,83.3,60.3 M92.1,88.6c-0.1,0.2-0.3,0.4-0.5,0.6c0.2,0,0.4,0.2,0.2,0.3c-0.4,0.4-0.9,0.8-1.4,1c0,0-0.2,0-0.3,0c-0.2,0.2-0.5,0.4-0.7,0.7c-0.2,0.2-1.3,0.1-1-0.2c0.5-0.4,0.9-0.9,1.4-1.3c0.3-0.2,0.6-0.5,0.8-0.8c0.1-0.2,0.2-0.3,0.4-0.4C91.3,88.3,92.3,88.2,92.1,88.6 M88.7,87.1C88.7,87.1,88.7,87.1,88.7,87.1c-0.8,0.5-1.5,1-2.2,1.5c-0.8,0.5-1.7,0.8-2.5,1.2c0,0,0,0,0,0c-0.1-0.1-0.2-0.1-0.3-0.1c-0.7,0.4-1.3,0.9-1.9,1.5c-0.1,0.1-0.2,0.2-0.3,0.3l0,0c0,0,0,0,0,0l-0.3,0.3c0,0,0,0,0,0c0,0,0,0,0,0c-0.1,0.1-0.3,0.3-0.4,0.4c-0.1,0.1-0.1,0.2-0.3,0.3c-0.1,0.1-0.4,0.1-0.4-0.1c0,0,0,0,0,0c-0.1,0.1-0.2,0.1-0.3,0.2c-0.1,0.1-0.2,0.1-0.3,0.2c0,0-0.1,0-0.1,0c0,0-0.1,0-0.1,0c-0.2,0.2-0.5,0.4-0.7,0.6c-0.4,0.4-0.8,0.7-1.1,1.2c0,0,0,0,0,0c0,0,0,0,0,0.1c0,0,0,0-0.1,0.1c0,0,0,0.1-0.1,0.1c0,0,0,0,0,0c0,0.1-0.1,0.1-0.1,0.2c0,0,0,0,0,0c0,0-0.1,0.1-0.2,0.1c0,0-0.1-0.1-0.1-0.1c0,0,0-0.1-0.1-0.1c-0.1-0.1-0.1-0.2-0.2-0.3c0,0,0,0,0,0c0,0,0-0.1,0-0.1c0.2-0.2,0.4-0.4,0.6-0.7c0,0,0,0,0,0c0.1-0.1,0.1-0.2,0.2-0.2c0.1-0.1,0.2-0.3,0.3-0.4c0-0.1,0.1-0.1,0.1-0.2c0.2-0.3,0.4-0.5,0.6-0.8c0,0,0,0,0,0c0,0,0.1-0.1,0.1-0.1c0.1-0.1,0.2-0.3,0.3-0.4c0.1-0.1,0.1-0.2,0.2-0.4l0,0l0,0c0,0,0,0,0-0.1c0.1-0.2,0.1-0.3,0.2-0.4c0,0,0,0,0,0l0-0.1c0-0.1,0-0.1,0.1-0.2c0,0,0,0,0,0c0-0.1,0-0.2,0.1-0.3c0,0,0-0.1,0-0.1c0.2-0.4,0.5-0.7,0.8-1c0,0-0.1,0-0.1,0c-0.3,0.2-0.5,0.4-0.7,0.6c-0.2,0.2-0.6-0.1-0.3-0.3c0.2-0.1,0.3-0.3,0.4-0.4c0,0,0,0,0,0c0.3-0.3,0.6-0.7,1-1c0.2-0.2,0.4-0.3,0.6-0.4c0,0,0.1-0.1,0.1-0.1c0.1-0.2,0.3-0.3,0.4-0.5c0,0,0,0,0,0c1.8-1.7,4.9-1.7,7.2-2.8c0.9-0.4,2.1,0.2,3,0c0.6,0,1.1,0,1.7,0.4C91.8,85,90.3,86.1,88.7,87.1 M92.6,73.9c-0.2-0.2,0.6,0,0.8-0.4h-1.5c-0.2,0-0.2-0.2-0.2-0.4c-0.9,0.2-2.1,0.6-3,0.8c-1.3,0.4-2.5,1.3-4,1.7c-2.1,0.8-3.8,2.5-6,3.2c-0.2,0-0.2-0.2-0.2-0.4c0.2-0.6,0.9-0.8,1.3-1.3c0-0.2,0-0.4-0.2-0.4c1.5-2.1,3.6-3.2,5.5-4.9v-0.6c0.6-0.8,1.5-1.1,1.9-2.1c0.2-0.6,1-1.3,1.9-1.7c-0.2-0.2-0.6-0.2-0.6-0.6c-0.8,0-1.5,0.4-2.3-0.2c0.4-0.3,0.8-0.5,1.2-0.7c-0.2,0-0.3-0.1-0.4-0.3c-0.2-0.4,0.4-0.8,0.9-0.9c0.8-0.2,1.7-0.2,2.3-0.8c-1.3-0.2-2.8,0.4-4.2-0.4c0.9-2.5,2.5-4.5,4.7-5.7c0.2,0,0.6,0,0.6,0.2c0,0.9-0.6,1.7-1.5,1.9c1.5,0.4,3,0.4,4.5,1.1c-0.2,0.4-0.6,0.2-0.8,0.2c0.9,0.6,2.1,0.2,3,0.9c-0.6,0.6-1.1,0-1.7,0c5.9,1.7,12.1,3,17,6.8c-4.2,2.1-8.5,3-13,4c-0.6,0-0.9,0-1.5-0.2c0,0.2,0,0.6-0.2,0.6c-0.8,0-1.3,0-1.9,0.4C94.3,74.3,93.2,74.5,92.6,73.9" /><path class="st2" d="M286.9,2.3H179.4c0,0,0.2,0,1,0.5c0.9,0.5,2,1.1,2.7,1.4c1.4,0.7,2.7,1.6,3.6,3c0.4,0.6,0.9,1.7,0.6,2.5c-0.4,0.9-0.6,2.5-1.5,2.8c-1.1,0.6-2.6,0.6-4,0.4c-0.8,0-1.5-0.2-2.3-0.4c2.8,1.1,5.5,2.5,7.4,5.1c0.2,0.4,0.9,0.6,1.7,0.6c0.2,0,0.2,0.4,0.2,0.6c-0.4,0.4-0.8,0.6-0.6,1.1h0.6c0.9-0.4,0.8-2.3,2.1-1.7c0.9,0.6,1.3,1.9,0.8,2.8c-0.8,0.8-1.5,1.3-2.3,1.9c-0.2,0.4-0.2,0.9,0,1.3c0.6,0.8,0.8,1.5,0.9,2.3c0.6,1.3,0.8,2.8,1.3,4.2c0.8,2.8,1.5,5.7,1.3,8.5c0,1.5-0.8,2.8-0.2,4.3c0.4,1.5,1.3,2.6,2.1,4c0.8,1.1,1.5,1.9,2.1,3c1.1,1.9,3.2,3.8,2.3,6c-0.6,1.3-2.6,1.1-4,1.9c-1.1,0.9-0.2,2.5,0.4,3.4c0.9,1.7-1.1,2.8-2.5,3.4c0.4,0.6,1.1,0.4,1.3,0.8c0.2,0.9,1.1,1.5,0.6,2.5c-0.8,1.1-3,1.7-1.9,3.4c0.8,1.3,0.3,2.8-0.2,4.2c-0.6,1.7-2.1,2.5-3.4,2.8c-1.1,0.4-2.5,0.4-3.6,0.2c-0.4-0.2-0.8-0.4-1.1-0.4c-3.2-0.4-6.4-1.3-9.6-1.3c-0.9,0.2-1.9,0.4-2.6,0.7c-0.9,0.6-1.6,1.3-2.3,2c0,0,0,0,0,0c-0.1,0.2-0.3,0.3-0.4,0.5c-0.1,0.1-0.2,0.2-0.2,0.3c-0.1,0.1-0.1,0.1-0.2,0.2c-0.6,0.7-1,1.4-1.5,2.2c0,0.1-0.1,0.1-0.1,0.1c0,0.1-0.1,0.2-0.2,0.3c-0.6,1.1-1.1,2.3-1.4,3.5c-1.3,4.3-0.7,8,0.2,8.9c0.2,0.2,6.2,2.1,10.4,4c2,0.9,3.3,1.5,4.5,2.3h105.6V2.3z" /><path class="st3"d="M185.8,38.7c0.8,0.2,1.9,0.2,1.9,0.6c-0.4,1.5-2.6,1.9-3.8,3.4h-0.6c-0.6,0.4-0.4,1.3-0.9,1.3c-0.6-0.2-1.1,0-1.7,0.2c0.8,0.8,1.7,1.3,2.8,1.1c0.2,0,0.6,0.4,0.6,0.8c0,0,0.2,0,0.4-0.2c0.2,0,0.4,0,0.4,0.2v0.8c-0.6,0.8-1.5,0.4-2.3,0.6c1.5,0.4,3,0.4,4.4,0c1.1-0.4,0-2.3,0.8-3.2c-0.4,0,0-0.6-0.4-0.6c0.4-0.4,0.8-0.9,1.1-1.1c0.4,0,0.9-0.2,1.1-0.6c0-0.4-0.8-0.6-0.6-0.9c1.1-0.8,2.1-1.9,1.7-3c-0.2-0.6-1.7-0.6-2.6-1c-0.9-0.4-2.1,0-3.2,0.2c-0.9,0-1.9,0.6-2.8,0.8c-1.3,0.4-2.5,1.1-3.6,1.9c1.3-0.6,2.6-0.8,4.1-1.1C183.7,38.7,184.6,38.5,185.8,38.7" /><pathd="M256.2,424.9c2.2,0,4.1,1.7,3.1,5.6l-10.1,2.7C250.8,428.4,253.8,424.9,256.2,424.9 M261.8,441.3h-2c-2.5,3-5.3,5.4-8,5.4c-2.8,0-4.2-1.7-4.2-5.4c0-1.5,0.2-3.1,0.5-4.5l16.4-5.4c3.2-7.6-0.7-10.9-5.2-10.9c-7.8,0-16.6,13.6-16.6,24.3c0,5.1,2.4,7.9,6.2,7.9C253.4,452.7,258,448.4,261.8,441.3 M259.2,416.9l9.3-8.5v-1.2h-6.2l-5.5,9.8H259.2z M224.3,425.1h5.4l-8.6,23.6c-0.8,2,0.3,4,2.4,4c6.1,0,13.4-5.2,16.2-12.6h-1.5c-2.2,3.1-7,6.5-10.6,7.2l7.9-22.2h8.1l1-3.4h-7.9l3-8.5h-3.1l-5.6,8.5l-6.7,0.9V425.1z M218.7,423.9c0.7-2.2-0.8-3.4-1.9-3.4c-4.7,0-10.4,4.3-12.6,10.2h1.5c1.5-2.2,4.1-4.6,6.6-5l-9.1,23.6c-0.8,2.2,0.8,3.4,2,3.4c4.5,0,9.8-4.3,12-10.2h-1.5c-1.5,2.2-4.1,4.6-6.6,5L218.7,423.9z M219.6,414.5c2,0,3.7-1.7,3.7-3.7c0-2-1.7-3.7-3.7-3.7c-2.1,0-3.7,1.7-3.7,3.7C215.9,412.9,217.5,414.5,219.6,414.5 M175.7,427.1c1.4,0,2.2,2.2,0,7.1l-6.4,14.2c-1.2,2.7,0.1,4.4,2.7,4.4c1.6,0,2.3-0.4,3-2.1l6.3-16.6c2.9-3.6,8.3-7.4,10.7-7.4c1.7,0,1.5,1.4,0.4,3.6l-9.7,18.5c-0.9,1.8,0.3,4,2.4,4c4.7,0,10.4-4.3,12.6-10.2H196c-1.5,2.2-4.1,4.6-6.6,5l8.3-16.8c1.1-2.1,1.6-4.1,1.6-5.7c0-2.7-1.5-4.5-4.4-4.5c-4.1,0-7.6,4.6-12.6,10.3v-4.4c0-3.1-1-5.9-3.8-5.9c-3.3,0-6.3,5.2-8.7,10.2h1.5C173,428.4,174.5,427.1,175.7,427.1 M169.2,427.7c1.1-3.9,0.5-7.2-2.4-7.2c-3.7,0-4.9,2.5-8.5,10.3v-4.4c0-3.1-1-5.9-3.8-5.9c-3.3,0-6.3,5.2-8.7,10.2h1.5c1.6-2.3,3.1-3.7,4.3-3.7c1.4,0,2.2,2.2,0,7.1l-6.4,14.2c-1.2,2.7,0.1,4.4,2.7,4.4c1.6,0,2.3-0.4,3-2.1L157,434c1.8-2.2,3.4-4.1,5.4-6.2H169.2z M134.3,424.9c2.2,0,4.1,1.7,3.1,5.6l-10.1,2.7C129,428.4,131.9,424.9,134.3,424.9 M139.9,441.3h-2c-2.5,3-5.3,5.4-8,5.4c-2.8,0-4.2-1.7-4.2-5.4c0-1.5,0.2-3.1,0.5-4.5l16.4-5.4c3.2-7.6-0.6-10.9-5.2-10.9c-7.8,0-16.6,13.6-16.6,24.3c0,5.1,2.4,7.9,6.2,7.9C131.5,452.7,136.1,448.4,139.9,441.3 M102.4,425.1h5.4l-8.6,23.6c-0.8,2,0.3,4,2.4,4c6.1,0,13.5-5.2,16.2-12.6h-1.5c-2.2,3.1-7,6.5-10.6,7.2l7.9-22.2h8.1l1-3.4h-7.9l3-8.5h-3.1l-5.6,8.5l-6.7,0.9V425.1z M73.7,443.5c0-7.3,8.1-17.2,12.7-17.2c1,0,2,0.1,2.8,0.4l-4.7,12.6c-2.7,3.3-6.9,7.3-8.9,7.3C74.4,446.6,73.7,445.7,73.7,443.5 M98.6,419.1l-2.5-0.2l-2.8,2.8h-0.5c-11.9,0-24.7,14.8-24.7,26.5c0,2.7,1.5,4.5,4.4,4.5c3.5,0,6.9-5,10.8-10.3l-0.2,1.9c-0.5,5.4,1.2,8.4,4,8.4c3.3,0,6.3-5.2,8.6-10.2h-1.5c-1.6,2.3-3.1,3.7-4.3,3.7c-1.2,0-2.1-2.3,0-7.1L98.6,419.1z M73.1,427.7c1.1-3.9,0.5-7.2-2.4-7.2c-3.7,0-4.9,2.5-8.5,10.3v-4.4c0-3.1-1-5.9-3.9-5.9c-3.3,0-6.3,5.2-8.6,10.2h1.5c1.6-2.3,3.1-3.7,4.3-3.7c1.4,0,2.2,2.2,0,7.1L49,448.4c-1.2,2.7,0.1,4.4,2.7,4.4c1.6,0,2.3-0.4,3-2.1L61,434c1.8-2.2,3.4-4.1,5.4-6.2H73.1z M31.2,451.6l0.6-1.8c-7.9-1.5-8.9-1.5-5.7-10.1l3-8.1h6.3c3.9,0,4,1.7,3.4,6h2.3l5.2-14.3h-2.3c-2,3.4-3.5,6-7.8,6h-6.3l4.3-11.7c1.5-4.2,2.2-5,7.6-5h1.4c5.5,0,6.2,1.5,6.2,7.3h2.2l1.8-9.7H22.9l-0.6,1.8c6.3,1.3,6.9,1.9,4,10.1l-6.5,17.7c-3,8.1-4.2,8.8-11.5,10.1l-0.5,1.8H31.2z" /><path d="M182.5,356c2.2,0,4.1,1.7,3.1,5.6l-10.1,2.7C177.1,359.5,180.1,356,182.5,356 M188.1,372.4h-2c-2.5,3-5.3,5.4-8,5.4c-2.8,0-4.2-1.7-4.2-5.4c0-1.5,0.2-3.1,0.5-4.5l16.4-5.4c3.2-7.6-0.7-10.9-5.2-10.9c-7.8,0-16.6,13.6-16.6,24.3c0,5.1,2.4,7.9,6.2,7.9C179.7,383.9,184.3,379.5,188.1,372.4 M185.5,348l9.3-8.5v-1.2h-6.2l-5.5,9.8H185.5z M150.6,356.2h5.4l-8.6,23.6c-0.8,2,0.3,4,2.4,4c6.1,0,13.4-5.2,16.2-12.6h-1.5c-2.2,3.1-7,6.5-10.6,7.2l7.9-22.2h8.1l1-3.4H163l3-8.5h-3.1l-5.6,8.5l-6.7,1V356.2z M145,355.1c0.7-2.2-0.8-3.4-2-3.4c-4.7,0-10.4,4.3-12.6,10.2h1.5c1.5-2.2,4.1-4.6,6.6-5l-9.1,23.6c-0.8,2.2,0.8,3.4,2,3.4c4.5,0,9.8-4.3,12-10.2h-1.5c-1.5,2.2-4.1,4.6-6.6,5L145,355.1z M145.9,345.7c2,0,3.7-1.7,3.7-3.7c0-2-1.7-3.7-3.7-3.7c-2.1,0-3.7,1.7-3.7,3.7C142.2,344,143.8,345.7,145.9,345.7 M116.9,378.7l15-39.8l-0.5-0.7l-10.4,1.2v1.2l2,1.5c1.8,1.4,1.2,2.7-0.4,7.2l-11.4,30.4c-1,1.8,0.3,4,2.4,4c4.7,0,9.8-4.3,12-10.2h-1.5C122.5,375.8,119.3,378.2,116.9,378.7M86.3,374.6c0-7.3,8.1-17.2,12.7-17.2c1,0,1.9,0.1,2.8,0.4L97,370.4c-2.7,3.3-6.9,7.3-8.9,7.3C87,377.8,86.3,376.8,86.3,374.6M111.2,350.3l-2.5-0.2l-2.8,2.8h-0.5c-11.9,0-24.7,14.8-24.7,26.5c0,2.7,1.5,4.5,4.4,4.5c3.5,0,6.9-5,10.8-10.3l-0.2,1.9c-0.5,5.4,1.2,8.4,4,8.4c3.3,0,6.3-5.2,8.6-10.2h-1.5c-1.6,2.3-3.1,3.7-4.3,3.7c-1.2,0-2.1-2.3,0-7L111.2,350.3z M53.3,389.6c0-3.1,3-5.1,7.3-6.8c1.4,0.7,3.6,1.5,6.4,2.4c4.5,1.5,6.2,2.1,6.2,3.4c0,2.9-4.1,5.1-11.6,5.1C56,393.8,53.3,392.6,53.3,389.6M65.6,370.5c-2,0-2.7-1.7-2.7-3.6c0-5.9,2.8-13,7.3-13c2,0,2.7,1.7,2.7,3.6C72.9,363.3,70,370.5,65.6,370.5 M78.4,386.7c0-3.8-3.4-5.2-8.9-6.8c-4.7-1.4-6.9-1.8-6.9-3.4c0-1.2,1-2.7,3-3.8c7.8-0.4,12.7-7.4,12.7-13.6c0-1.1-0.2-2.1-0.5-3h5.3l1-3.4h-9c-1.2-0.8-2.7-1.2-4.4-1.2c-8.2,0-13.5,7.2-13.5,13.6c0,4.1,2.4,6.9,6.2,7.4c-3.8,1.8-6,3.7-6,6.1c0,1.4,0.5,2.4,1.7,3.3c-8.8,2.6-12.4,5.9-12.4,9.7c0,4.1,5.4,5.8,11.8,5.8C69.3,397.5,78.4,391.6,78.4,386.7 M37.6,362.7c3.9,0,4,1.7,3.4,6h2.3l5.2-14.3h-2.3c-2,3.4-3.5,6-7.8,6h-8.7l4.3-11.7c1.5-4.2,2.3-5,7.6-5h3.8c5.5,0,6.2,1.5,6.2,7.3h2.2l1.8-9.7H22.9l-0.6,1.8c6.3,1.3,6.9,1.9,4,10.1l-6.5,17.7c-3,8.1-4.2,8.8-11.5,10.1l-0.5,1.8h36.4l6.5-10.3h-2.5c-4.2,4.2-8.5,7.9-16.6,7.9c-9.7,0-8.8-0.5-5.6-9.5l3-8.1H37.6z M42.3,338.3l9.3-6.8v-1.2h-6.2l-5.5,8H42.3z" /><path d="M181.3,287.2c2.2,0,4.1,1.7,3.1,5.6l-10.1,2.7C175.9,290.6,178.9,287.2,181.3,287.2 M186.9,303.6h-2c-2.5,3-5.3,5.4-8,5.4c-2.8,0-4.2-1.7-4.2-5.4c0-1.5,0.2-3.1,0.5-4.5l16.4-5.4c3.2-7.6-0.7-10.9-5.2-10.9c-7.8,0-16.6,13.6-16.6,24.3c0,5.1,2.4,7.9,6.2,7.9C178.5,315,183.1,310.7,186.9,303.6 M184.3,279.2l9.3-8.5v-1.2h-6.2l-5.5,9.8H184.3z M149.4,287.3h5.5l-8.6,23.6c-0.8,2,0.3,4,2.4,4c6.1,0,13.5-5.2,16.2-12.6h-1.5c-2.2,3.1-7,6.5-10.6,7.2l7.9-22.2h8.1l1-3.4h-7.9l3-8.5h-3.1l-5.6,8.5l-6.7,0.9V287.3z M146.6,290c1.1-3.9,0.5-7.2-2.4-7.2c-3.7,0-4.9,2.5-8.5,10.3v-4.4c0-3.1-1-5.9-3.8-5.9c-3.3,0-6.3,5.2-8.7,10.2h1.5c1.6-2.3,3.1-3.7,4.3-3.7c1.4,0,2.2,2.2,0,7.1l-6.4,14.2c-1.2,2.7,0.1,4.4,2.7,4.4c1.6,0,2.3-0.4,3-2.1l6.3-16.6c1.8-2.2,3.4-4.1,5.4-6.2H146.6z M111.7,287.2c2.2,0,4.1,1.7,3.1,5.6l-10.1,2.7C106.3,290.6,109.3,287.2,111.7,287.2 M117.3,303.6h-2c-2.5,3-5.3,5.4-8,5.4c-2.8,0-4.2-1.7-4.2-5.4c0-1.5,0.2-3.1,0.5-4.5l16.4-5.4c3.2-7.6-0.6-10.9-5.2-10.9c-7.8,0-16.6,13.6-16.6,24.3c0,5.1,2.4,7.9,6.2,7.9C108.9,315,113.5,310.7,117.3,303.6M79.1,310.2c-1.6,0-3.9-1.5-3.9-2.8c0-0.4,0.7-2.3,1.6-4.6l2.6-7c2.8-3.4,7.2-7.1,9.7-7.1c1.5,0,2.6,1,2.6,3.1C91.6,298.4,85.6,310.2,79.1,310.2 M97.3,289.3c0-4.8-1.2-6.6-4.6-6.6c-4.2,0-8.1,4.5-12.1,9.9L89,270l-0.5-0.7l-10.4,1.2v1.2l2,1.5c1.8,1.4,1.2,2.8-0.4,7.2l-9.1,23.9c-0.8,2-1.7,4.4-1.7,5c0,2.8,3.8,5.5,7.3,5.5C84.1,315,97.3,300.5,97.3,289.3M66.6,286.2c0.6-2.2-0.8-3.4-2-3.4c-4.7,0-10.4,4.3-12.6,10.2h1.5c1.5-2.2,4.1-4.6,6.6-5l-9.1,23.6c-0.8,2.2,0.8,3.4,2,3.4c4.5,0,9.8-4.3,12-10.2h-1.5c-1.5,2.2-4.1,4.6-6.6,5L66.6,286.2z M67.6,276.8c2,0,3.7-1.7,3.7-3.7c0-2-1.7-3.7-3.7-3.7c-2.1,0-3.7,1.7-3.7,3.7C63.9,275.1,65.5,276.8,67.6,276.8 M44.5,272.3H22.9l-0.6,1.8c6.3,1.3,6.9,1.9,4,10.1l-6.5,17.7c-3,8.1-4.2,8.8-11.5,10.1l-0.5,1.8h32.8l7.1-12.7h-2.5c-4.1,4.5-8.8,10.2-16.1,10.2c-5.5,0-6.3-1-3.2-9.5l6.5-17.7c3-8.1,4.2-8.8,11.5-10.1L44.5,272.3z" /></g></g></svg>'

IMPLEMENTED_COMPONENTS = {
    "accordion": {
        "title": "Accordéon",
        "sample_data": [
            {
                "id": "sample-accordion",
                "title": "Titre de l’objet accordéon",
                "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em></p>",
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/accordeon",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/accordion/",
    },
    "alert": {
        "title": "Alertes",
        "sample_data": [
            {
                "title": "Alerte refermable de type succès",
                "type": "success",
                "content": "Cliquer sur la croix pour fermer l’alerte.",
                "heading_tag": "h3",
                "is_collapsible": True,
                "id": "alert-success-tag",
            },
            {
                "title": "Alerte refermable de type erreur",
                "type": "error",
                "content": "Cliquer sur la croix pour fermer l’alerte.",
                "heading_tag": "h3",
                "is_collapsible": True,
            },
            {
                "title": "Alerte non-refermable de type info",
                "type": "info",
                "content": "Cette alerte n’a pas de croix de fermeture.",
                "heading_tag": "h3",
            },
            {
                "type": "warning",
                "heading_tag": "h3",
                "title": "Alerte medium sans contenu",
            },
            {
                "type": "warning",
                "content": "Petite alerte sans titre.",
                "extra_classes": "village-alert--sm",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/alerte",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/alert/",
    },
    "badge": {
        "title": "Badge",
        "sample_data": [
            {
                "label": "Badge simple",
                "extra_classes": "",
            },
            {
                "label": "Petit badge",
                "extra_classes": "village-badge--sm",
            },
            {
                "label": "Badge coloré",
                "extra_classes": "village-badge--green-menthe",
            },
            {
                "label": "Badge système",
                "extra_classes": "village-badge--success",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/badge",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/badge/",
    },
    "breadcrumb": {
        "title": "Fil d’Ariane",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/fil-d-ariane",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/breadcrumb/",
    },
    "button": {
        "title": "Boutons",
        "sample_data": [
            {
                "label": "Bouton principal",
                "onclick": "alert('Vous avez cliqué sur le bouton principal')",
            },
            {
                "label": "Bouton secondaire",
                "name": "secundary-button",
                "type": "button",
                "extra_classes": "village-btn--secondary",
                "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
            },
            {
                "label": "Bouton tertiaire",
                "extra_classes": "village-btn--tertiary",
                "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
            },
            {
                "label": "Bouton tertiaire sans bordure",
                "type": "button",
                "extra_classes": "village-btn--tertiary-no-outline",
                "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/button/",
    },
    "button_group": {
        "title": "Boutons – Groupe",
        "sample_data": [
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                        "extra_classes": "village-icon-checkbox-circle-line village-btn--icon-left",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "village-icon-checkbox-circle-line village-btn--icon-left village-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                ],
                "extra_classes": "btns-group--icon-left",
            },
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "village-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                    {
                        "label": "Bouton tertiaire",
                        "extra_classes": "village-btn--tertiary",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
                    },
                    {
                        "label": "Bouton tertiaire sans bordure",
                        "type": "button",
                        "extra_classes": "village-btn--tertiary-no-outline",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
                    },
                ],
                "extra_classes": "btns-group--equisized",
            },
            {
                "items": [
                    {
                        "label": "Bouton principal",
                        "onclick": "alert('Vous avez cliqué sur le bouton principal')",
                    },
                    {
                        "label": "Bouton secondaire",
                        "name": "secundary-button",
                        "type": "button",
                        "extra_classes": "village-btn--secondary",
                        "onclick": "alert('Vous avez cliqué sur le bouton secondaire')",
                    },
                    {
                        "label": "Bouton tertiaire",
                        "extra_classes": "village-btn--tertiary",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire')",
                    },
                    {
                        "label": "Bouton tertiaire sans bordure",
                        "type": "button",
                        "extra_classes": "village-btn--tertiary-no-outline",
                        "onclick": "alert('Vous avez cliqué sur le bouton tertiaire sans bordure')",
                    },
                ],
                "extra_classes": "btns-group--inline-sm",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/groupe-de-boutons",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/button/",
    },
    "callout": {
        "title": "Mise en avant",
        "sample_data": [
            {
                "title": "Mise en avant avec bouton normal",
                "text": "Cette mise en avant a un bouton normal",
                "icon_class": "village-icon-alert-line",
                "button": {
                    "onclick": "alert('Ce bouton est bien un bouton')",
                    "label": "Bouton normal",
                    "extra_classes": "village-btn--secondary",
                },
            },
            {
                "title": "Mise en avant avec lien",
                "text": "Cette mise en avant a un lien d’appel à action",
                "icon_class": "village-icon-external-link-line",
                "button": {
                    "label": "Bouton qui est un lien",
                    "url": "https://www.systeme-de-design.gouv.fr/",
                    "extra_classes": "village-btn--secondary",
                },
            },
            {
                "title": "Mise en avant en couleur",
                "text": "Cette mise en avant a une classe de couleur",
                "icon_class": "village-icon-palette-line",
                "extra_classes": "village-callout--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-avant",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/callout/",
    },
    "card": {
        "title": "Carte",
        "sample_data": [
            {
                "title": "Carte basique",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ cinq lignes dans le mode vertical, et deux en horizontal.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.16x9.svg",
                "new_tab": True,
            },
            {
                "title": "Carte horizontale, largeur standard",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "village-card--horizontal",
            },
            {
                "title": "Carte horizontale, largeur tiers",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "village-card--horizontal village-card--horizontal-tier",
            },
            {
                "title": "Carte horizontale, largeur moitié",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ deux lignes dans le mode horizontal, et cinq en vertical.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "extra_classes": "village-card--horizontal village-card--horizontal-half",
            },
            {
                "title": "Carte avec badge",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "media_badges": [
                    {
                        "label": "Nouveau",
                        "extra_classes": "village-badge--new",
                    }
                ],
            },
            {
                "title": "Carte avec détails d’en-tête (tags)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "top_detail": {
                    "detail": {
                        "icon_class": "village-icon-warning-fill",
                        "text": "Détail (optionnel) avec icône (optionnelle)",
                    },
                    "tags": [{"label": "tag 1"}, {"label": "tag 2"}],
                },
            },
            {
                "title": "Carte avec image et détails d’en-tête (badges)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "image_url": "/static/img/placeholder.16x9.svg",
                "top_detail": {
                    "detail": {
                        "icon_class": "village-icon-warning-fill",
                        "text": "Détail (optionnel)",
                    },
                    "badges": [
                        {"label": "Badge 1"},
                        {"extra_classes": "village-badge--warning", "label": "Badge 2"},
                    ],
                },
            },
            {
                "title": "Carte avec détails en pied",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "new_tab": True,
                "bottom_detail": {
                    "icon": "village-icon-warning-fill",
                    "text": "Détail (optionnel)",
                },
            },
            {
                "title": "Carte horizontale avec zone d’action (boutons)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "enlarge_link": False,
                "extra_classes": "village-card--horizontal",
                "call_to_action": {
                    "buttons": [
                        {"label": "Bouton 1", "extra_classes": "village-btn--secondary"},
                        {"label": "Bouton 2"},
                    ]
                },
            },
            {
                "title": "Carte horizontale avec zone d’action (liens)",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.1x1.svg",
                "new_tab": True,
                "enlarge_link": False,
                "extra_classes": "village-card--horizontal",
                "call_to_action": {
                    "links": [
                        {
                            "url": "/",
                            "label": "Lien interne",
                        },
                        {
                            "url": "https://www.systeme-de-design.gouv.fr/",
                            "label": "Lien externe",
                            "is_external": True,
                        },
                    ]
                },
            },
            {
                "title": "Carte avec un fond gris et une ombre",
                "description": """Texte de la carte.
                    Il peut prendre jusqu’à 200 caractères, ce qui devrait correspondre
                    à environ cinq lignes dans le mode vertical, et deux en horizontal.
                    """,
                "link": "https://www.systeme-de-design.gouv.fr/",
                "image_url": "/static/img/placeholder.16x9.svg",
                "new_tab": True,
                "extra_classes": "village-card--grey village-card--shadow",
            },
            {
                "title": "Carte sans lien",
                "description": """Peut être utile au besoin.""",
                "image_url": "/static/img/placeholder.1x1.svg",
                "enlarge_link": False,
                "extra_classes": "village-card--horizontal",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/carte",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/card/",
    },
    "consent": {
        "title": "Gestionnaire de consentement",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/gestionnaire-de-consentement",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/consent/",
        "sample_data": [
            {
                "title": "À propos des cookies sur Django-village",
                "content": """
                Bienvenue ! Nous utilisons des cookies pour améliorer votre expérience et les
                services disponibles sur ce site. Pour en savoir plus, visitez la page <a href="#">
                Données personnelles et cookies</a>. Vous pouvez, à tout moment, avoir le contrôle
                sur les cookies que vous souhaitez activer.
                """,
            }
        ],
    },
    "content": {
        "title": "Contenu média",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/contenu-medias",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/content/",
        "sample_data": [
            {
                "image_url": "/static/img/placeholder.16x9.svg",
                "caption": "Image en largeur normale et en 16x9",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "ratio_class": "village-ratio-16x9",
            },
            {
                "image_url": "/static/img/placeholder.16x9.svg",
                "caption": "Image en largeur normale et en 4x3",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "ratio_class": "village-ratio-4x3",
            },
            {
                "image_url": "/static/img/placeholder.16x9.svg",
                "caption": "Image plus large que la colonne de contenu",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
                "extra_classes": "village-content-media--lg",
            },
            {
                "svg": gov_svg,
                "caption": """Image SVG avec un lien dans la légende.
                                <a class="village-link" href="https://main--ds-gouv.netlify.app/example/component/content/"
                                    rel=noopener external'
                                    title="Source - Ouvre une nouvelle fenêtre" target='_blank'>Source</a>.""",
                "alt_text": "Silhouette stylisée représentant le soleil au-dessus de deux montagnes.",
            },
            {
                "iframe": {
                    "title": "Présentation du portail tubes",
                    "width": "894",
                    "height": "450",
                    "url": "https://tube-numerique-educatif.apps.education.fr/videos/embed/9d0b132d-f836-459a-9b9b-97b1a647232d",
                    "sandbox": "allow-same-origin allow-scripts allow-popups",
                },
                "ratio_class": "village-ratio-4x3",
                "caption": "Vidéo avec transcription",
                "alt_text": "",
                "transcription": {"content": f"<div>{lorem_ipsum}</div>"},
            },
        ],
    },
    "favicon": {
        "title": "Icône de favoris",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/icones-de-favoris",
        "example_url": "https://main--ds-gouv.netlify.app/example/core/favicon/",
    },
    "follow": {
        "title": "Lettre d’information et réseaux sociaux",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lettre-d-information-et-reseaux-sociaux",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/follow/",
    },
    "footer": {
        "title": "Pied de page",
    },
    "france_connect": {
        "title": "Bouton FranceConnect",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-franceconnect",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/connect/",
        "sample_data": [
            {},
            {"id": "france-connect-plus", "plus": True},
        ],
    },
    "header": {
        "title": "En-tête",
    },
    "highlight": {
        "title": "Mise en exergue",
        "sample_data": [
            {
                "content": "Contenu de la mise en exergue",
                "size_class": "village-text--sm",
            },
            {
                "content": "Mise en exergue avec bordure colorée",
                "extra_classes": "village-highlight--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mise-en-exergue",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/highlight/",
    },
    "input": {
        "title": "Champs de saisie",
        "sample_data": [
            {
                "id": "example-input-id",
                "label": "Label du champ de saisie",
                "type": "text",
                "onchange": "alert(value)",
                "value": "(Optionnel) valeur du champ de saisie",
            },
            {
                "label": "Champ de saisie de date",
                "type": "date",
                "onchange": "alert(value)",
                "value": "2021-09-16",
                "min": "2021-09-04",
                "max": "2021-09-23",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/champ-de-saisie",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/input/",
    },
    "link": {
        "title": "Lien",
        "sample_data": [
            {
                "url": "/django_village/components/link/",
                "label": "Lien interne",
            },
            {
                "url": "https://www.systeme-de-design.gouv.fr/",
                "label": "Lien externe, large",
                "is_external": True,
                "extra_classes": "village-link--lg",
            },
            {
                "url": "/django_village/components/link/",
                "label": "Petit lien interne avec flèche",
                "is_external": False,
                "extra_classes": "village-icon-arrow-right-line village-link--icon-right village-link--sm",
            },
            {
                "url": "/django_village/components/link/",
                "label": "Lien de téléchargement",
                "extra_classes": "village-link--download",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liens",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/link/",
    },
    "notice": {
        "title": "Bandeau d’information importante",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bandeau-d-information-importante",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/notice/",
        "sample_data": [
            {
                "title": """Label titre du bandeau d’information importante, comprenant un texte assez long
                            pour être sur deux lignes, et <a href='#'
                            rel='noopener external'
                            title="intitulé - Ouvre une nouvelle fenêtre" target='_blank'>
                            un lien au fil du texte</a>, ainsi qu’une croix de fermeture.""",
                "is_collapsible": True,
            }
        ],
    },
    "pagination": {
        "title": "Pagination",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/pagination",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/pagination/",
    },
    "quote": {
        "title": "Citation",
        "sample_data": [
            {
                "text": "Développer vos sites et applications en utilisant des composants prêts à l’emploi, accessibles et ergonomiques",  # noqa
                "source_url": "https://www.systeme-de-design.gouv.fr/",
                "author": "Auteur",
                "source": "Système de Design de l'État",
                "details": [
                    {"text": "Détail sans lien"},
                    {
                        "text": "Détail avec lien",
                        "link": "https://template.incubateur.net/",
                    },
                ],
                "image_url": "/static/img/placeholder.1x1.svg",
                "extra_classes": "village-quote--green-emeraude",
            },
            {
                "text": "Citation très basique, sans aucun des champs optionnels.",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/citation",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/quote/",
    },
    "select": {
        "title": "Listes déroulantes",
        "sample_data": [
            {
                "id": "select-example-id",
                "label": "Label de l’élément select",
                "onchange": "console.log(value)",
                "default": {
                    "disabled": True,
                    "hidden": True,
                    "text": "Choisissez une option",
                },
                "options": [
                    {"text": "Option 1", "value": 1},
                    {"text": "Option 2", "value": 2},
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/liste-deroulante",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/select/",
    },
    "sidemenu": {
        "title": "Menu latéral",
        "sample_data": [
            {
                "title": "Menu",
                "items": [
                    {
                        "label": "Menu replié",
                        "items": [
                            {
                                "label": "Une page",
                                "link": "#",
                            },
                            {
                                "label": "Une autre page",
                                "link": "/sidemenu",
                            },
                        ],
                    },
                    {
                        "label": "Menu ouvert",
                        "items": [
                            {
                                "label": "Sous-menu replié",
                                "items": [
                                    {"label": "Encore une page", "link": "#"},
                                ],
                            },
                            {
                                "label": "Sous-menu ouvert",
                                "items": [
                                    {"label": "Page non active", "link": "#"},
                                    {
                                        "label": "Page active",
                                        "link": "/django_village/components/sidemenu/",
                                    },
                                ],
                            },
                        ],
                    },
                ],
            }
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/menu-lateral",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/sidemenu/",
    },
    "skiplinks": {
        "title": "Liens d’évitement",
        "sample_data": [
            [
                {"link": "#contenu", "label": "Contenu"},
                {"link": "#navigation-header", "label": "Menu"},
            ]
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/lien-d-evitement",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/skiplink/",
    },
    "stepper": {
        "title": "Indicateur d’étapes",
        "sample_data": [
            {
                "current_step_id": "1",
                "current_step_title": "Titre de l’étape en cours",
                "next_step_title": "Titre de la prochaine étape",
                "total_steps": "3",
            },
            {
                "current_step_id": "4",
                "current_step_title": "Titre de la dernière étape",
                "total_steps": "4",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/indicateur-d-etapes",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/stepper/",
    },
    "summary": {
        "title": "Sommaire",
        "sample_data": [
            [
                {"link": "#", "label": "Titre du premier élément"},
                {"link": "#", "label": "Titre du second élément"},
            ],
            [
                {"link": "#", "label": "Titre du premier élément"},
                {
                    "link": "#",
                    "label": "Titre du second élément",
                    "children": [
                        {
                            "link": "#",
                            "label": "Titre du premier élément imbriqué",
                        },
                        {
                            "link": "#",
                            "label": "Titre du second élément imbriqué",
                            "children": [
                                {
                                    "link": "#",
                                    "label": "Titre du premier élément imbriqué (niveau inférieur)",
                                },
                                {
                                    "link": "#",
                                    "label": "Titre du second élément imbriqué (niveau inférieur)",
                                },
                            ],
                        },
                    ],
                },
            ],
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/sommaire",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/summary/",
    },
    "table": {
        "title": "Tableau",
        "sample_data": [
            {
                "caption": "Tableau basique",
                "header": ["Colonne 1", "Colonne 2", "Colonne 3"],
                "content": [["a", "b", "c"], ["d", "e", "f"]],
            },
            {
                "caption": "Tableau vert",
                "header": [
                    "Colonne 1",
                    "Colonne 2",
                    "Colonne 3",
                    "Colonne 4",
                    "Colonne 5",
                    "Colonne 6",
                ],
                "content": [
                    [
                        "Lorem ipsum dolor sit amet",
                        "consectetur adipiscing elit",
                        "sed do eiusmod tempor incididunt ut",
                        "labore et dolore magna aliqua",
                        "At quis risus sed vulputate odio ut enim",
                        100.0,
                    ],
                    [
                        "At risus viverra",
                        "adipiscing at in tellus",
                        "integer feugiat",
                        "Aliquam purus sit amet luctus venenatis lectus",
                        "Pellentesque id nibh tortor id aliquet lectus proin",
                        2,
                    ],
                ],
                "extra_classes": "village-table--green-emeraude village-table--bordered",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tableau",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/table/",
    },
    "tag": {
        "title": "Tag",
        "sample_data": [
            {"label": "Tag simple"},
            {"label": "Tag avec lien", "link": "/django_village/components"},
            {
                "label": "Petit tag avec icône",
                "extra_classes": "village-tag--sm village-icon-arrow-right-line village-tag--icon-left",  # noqa
            },
            {
                "label": "Tag avec action",
                "link": "#",
                "extra_classes": "village-icon-cursor-line village-tag--icon-right",
                "onclick": "alert('clicked'); return false;",
            },
            {
                "label": "Tag sélectionnable",
                "is_selectable": True,
            },
            {
                "label": "Tag supprimable",
                "is_dismissable": True,
            },
            {
                "label": "Tag vert",
                "link": "#",
                "extra_classes": "village-tag--green-emeraude",
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tag",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tag/",
    },
    "theme_modale": {
        "title": "Paramètres d’affichage",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/parametre-d-affichage",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/display/",
    },
    "tile": {
        "title": "Tuile",
        "sample_data": [
            {
                "title": "Tuile basique (verticale, MD)",
                "url": "/",
                "image_path": static("img/placeholder.1x1.svg"),
            },
            {
                "title": "Tuile horizontale",
                "description": "Tuile horizontale (MD)",
                "detail": "Avec un pictogramme SVG",
                "url": "/",
                "id": "tile-cityhall",
                "extra_classes": "village-tile--horizontal",
                "svg_path": static("django_village/dist/artwork/pictograms/buildings/city-hall.svg"),
            },
            {
                "title": "Tuile verticale (SM)",
                "url": "/",
                "id": "tile-nuclear-plant",
                "extra_classes": "village-tile--sm",
                "svg_path": static("django_village/dist/artwork/pictograms/buildings/nuclear-plant.svg"),
            },
            {
                "title": "Tuile horizontale (SM)",
                "url": "/",
                "id": "tile-map",
                "extra_classes": "village-tile--horizontal village-tile--sm",
                "top_detail": {
                    "badges": [
                        {
                            "label": "Badge coloré",
                            "extra_classes": "village-badge--sm village-badge--purple-glycine",
                        },
                    ]
                },
                "svg_path": static("django_village/dist/artwork/pictograms/map/map.svg"),
            },
            {
                "title": "Tuile à fond gris et ombre sans bordure",
                "url": "/",
                "id": "tile-map",
                "extra_classes": "village-tile--horizontal village-tile--grey village-tile--shadow village-tile--no-border",
                "svg_path": static("django_village/dist/artwork/pictograms/leisure/paint.svg"),
            },
            {
                "title": "Tuile de téléchargement",
                "extra_classes": "village-tile--horizontal village-tile--download",
                "detail": "PDF — 1,7 Mo",
                "url": "/",
                "svg_path": static("django_village/dist/artwork/pictograms/document/document-signature.svg"),
            },
        ],
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/tuile",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tile/",
    },
    "toggle": {
        "title": "Interrupteur",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/interrupteur",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/toggle/",
        "sample_data": [
            {
                "label": "Interrupteur basique",
            },
            {
                "label": "Interrupteur basique désactivé avec aide",
                "help_text": "Vous ne pouvez pas utiliser cet interrupteur.",
                "is_disabled": True,
            },
            {
                "label": "Interrupteur complet aligné à gauche",
                "help_text": "Cet interrupteur présente toutes les options disponibles",
                "is_disabled": False,
                "extra_classes": "village-toggle--label-left village-toggle--border-bottom",
                "id": "toggle-full",
            },
        ],
    },
    "tooltip": {
        "title": "Infobulle",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/infobulle",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tooltip/",
        "sample_data": [
            {
                "content": "Contenu d’une infobule activée au survol",
                "label": "Libellé du lien",
            },
            {
                "content": "Contenu d’une infobule cliquable",
                "is_clickable": True,
                "id": "tooltip-b",
            },
        ],
    },
    "transcription": {
        "title": "Transcription",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/transcription",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/transcription/",
        "sample_data": [
            {
                "content": "<div><p>Courte transcription basique</p></div>",
            },
            {
                "title": "Transcription très longue",
                "content": f"<div>{lorem_ipsum}</div>",
            },
        ],
    },
}

EXTRA_COMPONENTS = {
    "accordion_group": {
        "title": "Accordéons – Groupe",
        "sample_data": [
            [
                {
                    "id": "sample-accordion-1",
                    "title": "Premier accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (1)</p>",  # noqa
                },
                {
                    "id": "sample-accordion-2",
                    "title": "Deuxième accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (2)</p>",  # noqa
                },
                {
                    "id": "sample-accordion-3",
                    "title": "Troisième accordéon",
                    "content": "<p>Contenu d’exemple avec du <strong>gras</strong> et de l’<em>italique</em> (3)</p>",  # noqa
                },
            ]
        ],
    },
    "badge_group": {
        "title": "Badges – Groupe",
        "sample_data": [
            [
                {
                    "label": "Succès",
                    "extra_classes": "village-badge--success",
                },
                {
                    "label": "Info",
                    "extra_classes": "village-badge--info",
                },
                {
                    "label": "Avertissement",
                    "extra_classes": "village-badge--warning",
                },
                {
                    "label": "Erreur",
                    "extra_classes": "village-badge--error",
                },
                {
                    "label": "Nouveau",
                    "extra_classes": "village-badge--new",
                },
            ]
        ],
    },
    "css": {"title": "CSS global"},
    "js": {"title": "JS global"},
    "form": {"title": "Formulaire"},
    "form_field": {"title": "Formulaire - champ"},
    "django_messages": {
        "title": "Messages Django dans une alerte",
        "sample_data": [{"is_collapsible": True}],
    },
}

unsorted_IMPLEMENTED_COMPONENTS = {**IMPLEMENTED_COMPONENTS, **EXTRA_COMPONENTS}
ALL_IMPLEMENTED_COMPONENTS = dict(sorted(unsorted_IMPLEMENTED_COMPONENTS.items(), key=lambda k: k[1]["title"]))

NOT_YET_IMPLEMENTED_COMPONENTS = {
    "radio_rich": {
        "title": "Bouton radio riche",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/bouton-radio-riche",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/radio/",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#126](https://github.com/numerique-gouv/django_village/issues/126)
        """,
    },
    "segmented_control": {
        "title": "Contrôle segmenté",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/controle-segmente",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/segmented/",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#128](https://github.com/numerique-gouv/django_village/issues/128)
        """,
    },
    "range": {
        "title": "Curseur",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/curseur-range",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/range/",
        "note": """À implémenter au sein des formulaires et non comme une balise.
        cf. [#129](https://github.com/numerique-gouv/django_village/issues/129)
        """,
    },
}

# There is no need for specific tags for these
# (either because the village is implemented globally or because they are
# broken down into more specific tags)
WONT_BE_IMPLEMENTED = {
    "back_to_top": {
        "title": "Retour en haut de page",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/retour-en-haut-de-page",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/link/back-to-top/",
        "reason": "Utilisez une balise Lien (`village_link`)",
    },
    "checkbox": {
        "title": "Case à cocher",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/case-a-cocher",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/checkbox/",
        "reason": "Champ de formulaire.",
    },
    "download": {
        "title": "Téléchargement de fichier",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/telechargement-de-fichier",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/download/",
        "reason": "Pas un composant mais une série de variantes d’autres composants : [lien](/django_village/components/link/), [carte](/django_village/components/card/), [tuile](/django_village/components/tile/). Voir la documentation de ceux-ci.",
    },
    "file_upload": {
        "title": "Ajout de fichier",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/ajout-de-fichier",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/upload/",
        "reason": "Champ de formulaire.",
    },
    "modal": {
        "title": "Modale",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/modale",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/modal/",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "navigation": {
        "title": "Navigation principale",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/navigation-principale",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/navigation/",
        "reason": "Partie de l’en-tête, voir la documentation de ce composant.",
    },
    "password": {
        "title": "Mot de passe",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/mot-de-passe",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/password/",
        "reason": "Dépendant de l’implémentation des comptes utilisateurs dans le projet Django",
    },
    "radio": {
        "title": "Bouton radio",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/boutons-radio",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/radio/",
        "reason": "Champ de formulaire.",
    },
    "search_bar": {
        "title": "Barre de recherche",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/barre-de-recherche",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/search/",
        "reason": "Champ de formulaire.",
    },
    "share": {
        "title": "Partage",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/partage",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/share/",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "tab": {
        "title": "Onglet",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/onglet",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/tab/",
        "reason": "Une balise rendrait l’utilisation plus complexe au lieu de la simplifier.",
    },
    "translate": {
        "title": "Sélecteur de langue",
        "doc_url": "https://www.systeme-de-design.gouv.fr/elements-d-interface/composants/selecteur-de-langue",
        "example_url": "https://main--ds-gouv.netlify.app/example/component/translate/",
        "reason": "Partie de l’en-tête, voir la documentation de ce composant.",
    },
}

all_tags_unsorted = {
    **IMPLEMENTED_COMPONENTS,
    **EXTRA_COMPONENTS,
    **NOT_YET_IMPLEMENTED_COMPONENTS,
    **WONT_BE_IMPLEMENTED,
}
ALL_TAGS = dict(sorted(all_tags_unsorted.items()))
