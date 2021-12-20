<?php
    include 'document_header.php';
?>
    <body>
        <!--
        HTML: It can be good to use abstraction with different aspects of your website.
        For example, if you want to make a change to the navigation bar on your website,
        rather than having to go through changing it in every page, you can keep the navigation in 
        a separate document, allowing you to only need to change it once.
        You can use php to do this.
        Example: separate the header from the rest of the pages
        Steps: 
            Cut the header up to doctype and place in separate document
            Place a php tag where the header used to be, will be used to link the doc
            Use the include tag, and put the file path in single quotes as shown

        Using this method also allows you to include documents containg functions to be used in the program
        Similar to #include something.h
        -->
    </body>
</html>