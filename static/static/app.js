$(document).ready(function() {
    $("#aboutDiv").load("/Resources/about_section.txt", function(){
        $.ajax({
            type: "GET",
            url: "/about",
            timeout: 800000,
            success: function (data) {
                $("#aboutDiv").text(data);
                console.log("SUCCESS : ", data);
                alert("Done Loading");
            },
            error: function (e) {
                $("#aboutDiv").text(e.responseText);
                console.log("ERROR : ", e);
            }
        });
    });
    
    $("#btnGenerate").click(function (event) {
 
        //stop submit the form, we will post it manually.
        event.preventDefault();
 
        // Get form
        var form = $('#userUpload')[0];
 
       // Create an FormData object 
        var data = new FormData(form);
 
       // disabled the submit button
        $("#btnGenerate").prop("disabled", true);
 
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/userGenerate",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 800000,
            success: function (data) {
 
                $("#output").text(data);
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


    $("#btnSubmit").click(function (event) {
 
        //stop submit the form, we will post it manually.
        event.preventDefault();
 
        // Get form
        var form = $('#userUpload')[0];
 
       // Create an FormData object 
        var data = new FormData(form);
 
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