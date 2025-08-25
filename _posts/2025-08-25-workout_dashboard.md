---
layout: post
title: Building My First Tableau Dashboard from Smartwatch Data 
date: 2025-08-25 15:00:00
description: My workout dashboard in Tableau Public using data collected from Apple Watch.
tags: tableau workout fitness 
thumbnail: assets/img/workout.png
categories: data-visualisation
type: showcase
related_posts: true
---

This blog walks through how I built a personal fitness dashboard in **Tableau Public** using data collected from my **Apple Watch**.  
The process is straightforward — from extracting raw data to creating a clean, interactive dashboard.

**Step 1: Extract Data from Smartwatch**  
- Collected workout data from the **Apple Watch** and exported the data into `.gpx` files, which contain the GPS tracks, distance, and activity metrics.

**Step 2: Prepare Data with Power Query**  
- Opened the exported files in **Power Query (Excel/Power BI)**. Transformed and cleaned the workout metrics (distance, pace, time, activity type), then saved the output as an **XLSX file**, making it ready for Tableau.  


**Step 3: Transform GPS Data**  
- Had to convert the `.gpx` files into **XML format** for preparation.  Then Loaded the XML files into Power Query and consolidated the GPS route data to create a dataset suitable for mapping.  

**Step 4: Create Tableau Sheets**  
In Tableau, I built different sheets to capture different aspects of the data:
- **Workout Summary** – Total workouts, distance, best pace, average time.  
- **Trend Analysis** – Distance over time across years per activity type.  
- **Recent Workouts** – Distances and pace for the last 5 days.  
- **Elevation Profile** – Visualizing elevation changes per workout.  
- **Workout Map** – Showing cities/towns where I have done some workouts.  

**Step 5: Build the Dashboard**  
- Finally, I combined all the sheets into a single **interactive dashboard**. Added filters for **Year, Activity Type, and Location** and published the dashboard to **Tableau Public** for sharing.  

**Key Takeaway**  
This project gave me hands-on experience with:
- **Data extraction** from wearables  
- **Data cleaning and transformation** using Power Query  
- **Visualization** in Tableau  

It’s a great way to turn personal fitness data into meaningful insights while learning how to manage and visualize data across platforms.
<div>
<div class='tableauPlaceholder' id='viz1756139418423' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;KT&#47;KTD22YFD9&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;KTD22YFD9' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;KT&#47;KTD22YFD9&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1756139418423');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='2327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
</div>
