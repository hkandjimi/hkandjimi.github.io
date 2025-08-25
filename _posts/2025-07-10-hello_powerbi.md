---
layout: post
title: Chocolate Sales Dashboard - Hello PowerBI/Tableau
date: 2025-07-10 13:00:00
description: Learning Data analytics and visualisation through Youtube.
tags: powerbi tableau
categories: data-visualisation
thumbnail: assets/img/hellopowerbi.png
type: showcase
related_posts: true
---


This post shares my journey of creating my very first **Power BI dashboard** by following a helpful YouTube tutorial.  
The dashboard shown below is a rough recreation in **Tableau Public** of the one demonstrated in the video.  

🔗 Tutorial Link: [Watch on YouTube](https://www.youtube.com/watch?v=al4OfLIOl2w)

---

**📌 What I Learned**  

**1. Introduction to Power BI**  
- how to get started with Power BI, including downloading and installing **Power BI Desktop**, loading data, and creating visuals and tables. 

**2. Creating a Business Report**  
- step-by-step process of creating a complete business report using Power BI, from **loading and preparation of sample data** to formatting visuals and sharing the report with others.  

**3. Power BI Interface**  
- the main areas of the Power BI interface, including the **ribbon, canvas, panels, and switching panel**, and how to use these areas to construct and navigate reports. 

**4. Building Visuals**  
- how to create various types of visuals, such as **column charts, bar charts, and slicers**, and how to format and customize these visuals to **display data effectively**  

**5. Publishing and Sharing Reports**  
- the process of saving, publishing, and sharing Power BI reports, including the benefits of using the Power BI online platform for collaboration and data updates.  

---

**Final Thoughts 💭**  
This was my **first step into Power BI**—a powerful tool for turning raw data into meaningful insights.  
To further strengthen my skills and **enhance competence across different platforms**, I recreated the same dashboard in **Tableau Public**.  

Below is an embedded version of the recreated dashboard for easy access and exploration followed by screenshots from PowerBI:
<div>
<div class='tableauPlaceholder' id='viz1756133709306' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GJ&#47;GJXBFXDHY&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;GJXBFXDHY' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GJ&#47;GJXBFXDHY&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1756133709306');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script></div>

## Screenshots from PowerBI
<swiper-container keyboard="true" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true">
    {% for image in site.static_files %}
        {% if image.path contains 'img/choc_sales/' %}
          {%assign url = site.baseurl | append: image.path %}
          <swiper-slide>{% include figure.liquid loading="eager" path=url class="img-fluid rounded z-depth-1" %}</swiper-slide>
        {% endif %}
    {% endfor %}
</swiper-container>












