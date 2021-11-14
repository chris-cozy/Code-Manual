<!DOCTYPE html>
<html>
    <head>
        <meta charset= "UTF-8">
        <title>Calculator</title>
    </head>
    <body>
        <!--First php mini project to exercise current knowledge-->
        <!--Two inputs, then a drop down to decide the operation, and a calculate button -->
        <form>
            <!--Have to include a name so that you can use the info with php -->
            <input type="text" name="num1" placeholder="Number 1">
            <input type="text" name="num2" placeholder="Number 2">
            <select name="operator">
                <option>None</option>
                <option>Add</option>
                <option>Subtract</option>
                <option>Multiply</option>
                <option>Divide</option>
            </select>
            <br>
            <button type="submit" name="submit" value="submit">Calculate</button>
        </form>
        <!--Php often fetches the information it needs from the url -->
        <p> Answer is: </p>
        <?php
            //Check if calculate button has been hit
            if (isset($_GET['submit'])){
                $result1 = $_GET['num1'];
                $result2 = $_GET['num2'];
                $opp = $_GET['operator'];

                switch($opp){
                    case "None":
                        echo "You need to select a method.";
                        break;
                    case "Add":
                        echo $result1 + $result2;
                        break;
                    case "Subtract":
                        echo $result1 - $result2;
                        break;
                    case "Mulitply":
                        echo $result1 * $result2;
                        break;
                    case "Divide":
                        echo $result1 / $result2;
                        break;
                }
            }


        ?>
    </body>
</html>
