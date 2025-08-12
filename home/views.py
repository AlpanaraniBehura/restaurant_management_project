<!DOCTYPE html>
<html>
<head>
    <title>{{ restaurant_name }} Menu</title>
    <style>
        body{
          font-family:Arial,sans-serif;
          margin:20px;
          background:#fafafa;
        }

        nav a{
          margin-right: 15px;
          text-decoration: none;
          color: #333;
        }
        img{
          display:block;
          margin:20px auto;
          max-width:800px;
          border-radius: 10px;
        }

        ul{
          list-style:none;
          padding:0;
        
        }

        li{
          margin-bottom: 15px;
          padding: 10px;
          background:#f4f4f4;
          border-radius: 5px;
        }
    </style>
</head>

<body>
    <nav>
        <a href="{% url 'homepage'}">Home</a> |
        <a href="{% url 'about' %}">About Us</a>
    </nav>
    <h1>{{restaurant_name}}</h1>
    <h2>Our Menu</h2>
    <ul>
        {% for item in menu_items %}
        <li>
            <strong>{{ item.name }}</strong> - Rs.{{ item.price }}<br> {{ item.description }}
        </li>
        {% empty %}
        <li>No Menu items available.</li>
        {% endfor %}
    </ul>
</body>
</html>
          