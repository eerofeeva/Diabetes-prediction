$(document).ready(function() {
    $("#aboutDiv").load("/Resources/about_section.txt", function(){
        $.ajax({
            type: "GET",
            url: "/about",
            timeout: 800000,
            success: function (data) {
                $("#aboutDiv").html(data);
                console.log("SUCCESS : ", data);
            },
            error: function (e) {
                $("#aboutDiv").text(e.responseText);
                console.log("ERROR : ", e);
            }
        });
    });

    //load initial plotly graph


    $("#btnGenerate").click(function (event) {
 
        //stop submit the form, we will post it manually.
        event.preventDefault();
 
       // disabled the submit button
        $("#btnGenerate").prop("disabled", true);
 
        $.ajax({
            type: "POST",
            url: "/userGenerate",
            dataType: "json",
            cache: false,
            timeout: 800000,
            success: function (data) {
 
                $("#output").text(data.msg);
                var user = {age:parseInt(data.age), 
                            bmi:parseFloat(data.BMI)};
                var graph = DrawGraph(user);
                console.log("SUCCESS : ", data);
                $("btnGenerate").prop("disabled", false);
 
            },
            error: function (e) {
                $("#output").text(e.responseText);
                console.log("ERROR : ", e);
                $("#btnGenerate").prop("disabled", false);
            }
        });
    });

    //usersubmit 
    $("#btnSubmit").click(function (event) {
 
        //stop submit the form, we will post it manually.
        event.preventDefault();
 
        // Get form
        var form = $('#userUpload')[0];
 
       // Create an FormData object 
        var data = new FormData(form);
        
        var user = {age:parseInt(data.get("age")), bmi:(703*parseFloat(data.get("weight"))/parseFloat(data.get("height")) ** 2)};

        var graph = DrawGraph(user);

       // disabled the submit button
        $("#btnSubmit").prop("disabled", true);
 
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/userUpload",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
 
                $("#output").text(data);
                console.log("SUCCESS : ", data);
                $("#btnSubmit").prop("disabled", false);
 
            },
            error: function (e) {
 
                $("#output").text(e.responseText);
                console.log("ERROR : ", e);
                $("#btnSubmit").prop("disabled", false);
 
            }
        });
    });
});