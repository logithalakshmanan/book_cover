# Ex03 Time Table
# Date:29/11/20225
# AIM
To write a html webpage page to display your slot timetable.

# ALGORITHM
## STEP 1
Create a Django-admin Interface.

## STEP 2
Create a static folder and inert HTML code.

## STEP 3
Create a simple table using `<table>` tag in html.

## STEP 4
Add header row using `<th>` tag.

## STEP 5
Add your timetable using `<td>` tag.

## STEP 6
Execute the program using runserver command.

# PROGRAM
'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title Slot Time Table-LOGITHA></title>
</head>
<body>
    <img src="{% static 'logo.png' %}">
    <div class="title-box">Saveetha Engineering College</div>
    <div class="subtitle">SLOT TIME TABLE - LOGITHA </div>

    <style>
    body{
        font-family: 'Times New Roman', Times, serif;
        background-color: rgb(193, 223, 224);
    }

    table{
        width: 95%;
        margin: auto;
        border-collapse: collapse;
        font-size: 18px;
    }
    th{
        background-color: indianred;
        padding: 10px;
        border-radius: 1px;
        text-align: center;
        font-weight: bold;
    }
    td{
        padding:10px;
        border-radius: 1px;
        text-align: center;
        background-color: lavenderblush;
    }
    .title-box{
        text-align: center;
        font-size: 32px;
        font-weight: bold;

    }
    .subtitle{
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    .logo{
        display: block;
        align-items: center;
        margin-left: auto;
        margin-right: auto;
        width: 55%;
    }
    </style>

    <table border="3">
        <tr>
            <th>Day/Time</th>
            <th>Monday</th>
            <th>Tuesday</th>
            <th>Wednesday</th>
            <th>Thursday</th>
            <th>Friday</th>
            <th>Saturday</th>
        </tr>
        <tr>
            <th>8-10</th> 
            <td>WEB</td>
            <td>WEB</td>
            <td>WEB</td>
            <td>FREE SLOT</td>
            <td>FREE SLOT</td>
            <td>PYTHON</td>
        </tr>
        <tr>
            <th>10-12</th>
            <td>ENGLISH</td>
            <td>PYTHON</td>
            <td>FREE SLOT</td>
            <td>FREE SLOT</td>
            <td>ENGLISH</td>
            <td>ENGLISH</td>
        </tr>
        
        <tr>
            
            <td COLSPAN= 7 ALIGN="CENTER">LUNCH BREAK</td>
        </tr>
        <tr>
            <th>1-3</th>
            <td>WEB</td>
            <td>FREE SLOT</td>
            <td>MENTOR MEET</td>
            <td>FREE SLOT</td>
            <td>WEB</td>
            <td>ENGLISH</td>
        </tr>
        <tr>
            <th>3-5</th>
            <td>FREE SLOT</td>
            <td>PYTHON</td>
            <td>PYTHON</td>
            <td>PYTHON</td>
            <td>FREE SLOT</td>
            <td>FREE SLOT</td>
        </tr>
    </table>

    <h3 style="text-align: center; font-size: 20px;">Subjects</h3>
    <table border="3">
        <tr>
            <th>S. No.</th>
            <th>Subject Code</th>
            <th>Subject Name</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>19AI414</td>
            <td>Fundamentals of Web Application Development (WEB)</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>19EN101</td>
            <td>Communicative English (ENGLISH)</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>19AI301</td>
            <td>Python Programming (PYTHON)</td>
        </tr>
        
    </table>
</body>
</html>
'''
# OUTPUT
[alt text](image.png)





# RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
