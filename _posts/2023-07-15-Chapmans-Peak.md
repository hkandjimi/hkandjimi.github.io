---
layout: post
title: Chapman's Peak Drive
date: 2023-07-15 11:46:00
description: Two oceans drive through Chapman's peak drive, started in Grassy park all the way round to Noordhook and then back to the southern suburbs. 
tags: capetown bmw
categories: weekend-drive
thumbnail: assets/img/chapmans.jpeg
images:
  compare: true
  slider: true
---
Saturday drive trying to kill time and see places around Cape Town, was interested in the Chapman's Peak drive so decided to mimic the 2 oceans marathon path. Very scenic drive and full of parking spots on the sides for photos but unfortunate for me I didn't do much of that.

<div class="videoWrapper">
  <!-- Copy & Pasted from YouTube -->
  <iframe width="1276" height="718" src="https://www.youtube.com/embed/I3IoNr3cMKI" title="Chapman&#39;s Peak Drive" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


## A few random pictures
Below are a few random pictures taken on the drive, could have done better and most especially provide improved quality with better equipment.

<swiper-container keyboard="true" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true">
    {% for image in site.static_files %}
        {% if image.path contains 'img/chapmans/' %}
          {%assign url = site.baseurl | append: image.path %}
          <swiper-slide>{% include figure.liquid loading="eager" path=url class="img-fluid rounded z-depth-1" %}</swiper-slide>
        {% endif %}
    {% endfor %}
</swiper-container>



