import os
compile1 = 'sass shopHomepageBuild.scss ../css/shop-homepage.css'
compile2 = 'sass homeBuild.scss ../css/home.css'
compile3 = 'sass aboutBuild.scss ../css/about.css'

os.system(compile1)
os.system(compile2)
os.system(compile3)
