---
layout: default
permalink: /price/
title: Survey
---
<head>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/material-design-lite/material.min.css" rel="stylesheet">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/material-design-lite/material.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  
  <style>
    body {
      font-family: "Roboto", "Arial", sans-serif;
      background-image:url('/assets/img/Samsung-Galaxy.jpg');
      background-size: auto 100%;
      background-position: center;
      margin: 20px;
    }
    .card {
      margin: 20px 0;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      background-color: #ffffff;
    }
    .img-container {
      display: flex;
      justify-content: center;
      position: relative;
      padding: 5rem;
    }
    /* Centered text */
    .centered {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    *{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

.hero{
    width: 45rem;
    background-image: linear-gradient(rgba(250, 248, 248, 0.6), 
    rgba(250, 248, 248, 0.6)), url(background.jpg);
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #fff;
    border-radius: 15px;
    margin-top: -100px;
}

h1{
    font-size: 4rem;
    font-weight: 500;
    margin-bottom: 20px;
}

.timebox{
    display: flex;
    gap: 70px;
}

.time{
    text-align: center;
    font-weight: 100;
}

.time h2{
    font-size: 5rem;
    font-weight: 100;
}


  </style>
</head>
<body>
<div class="img-container">
    <!-- <img src="/assets/img/galaxy_tab_a99.png" class="img-fluid" alt="Responsive image"> -->
    <picture>
        <source media="(min-width: 961px)" srcset="/assets/img/galaxy_tab_a99.png">
        <source media="(min-width: 480px)" srcset="/assets/img/galaxy_tab_a9.png">
        <img src="/img/mobile-size.png"/>
    </picture>
    <div class="centered"> 
      <div class="hero">
        <video autoplay loop muted plays-inline width="720">
            <source src="/assets/img/winner_spinner.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </div>
  <!-- <script>
    const Days = document.getElementById('days');
    const Hours = document.getElementById('hours');
    const Minutes = document.getElementById('minutes');
    const Seconds = document.getElementById('seconds');
    const targetDate = new Date("March 7 2025 17:00:00").getTime();
    function pad2(number) {
      return (number < 10 ? '0' : '') + number
    }
    function timer () {
        const currentDate = new Date().getTime();
        const distance = targetDate - currentDate;
        const days = Math.floor(distance / 1000 / 60 / 60 / 24);
        const hours = Math.floor(distance / 1000 / 60 / 60) % 24;
        const minutes = Math.floor(distance / 1000 / 60) % 60;
        const seconds = Math.floor(distance / 1000) % 60;
        Days.innerHTML = pad2(days);
        Hours.innerHTML = pad2(hours);
        Minutes.innerHTML = pad2(minutes);
        Seconds.innerHTML = pad2(seconds);
        if(distance < 0){
            Days.innerHTML = "00";
            Hours.innerHTML = "00";
            Minutes.innerHTML = "00";
            Seconds.innerHTML = "00";
        }
    }
    setInterval(timer, 1000);
  </script> -->
</body>


