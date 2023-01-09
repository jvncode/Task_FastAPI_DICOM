function server_connect(path) {
    fetch('/'+path)
        .then(response => response.json())
        .then(json => $('#message').html('<center>\
        <h4 style = "color: black; background-color:#e3d193; margin-top: 10%;\
        border: 2px solid black; border-radius:22px; width:300px; height:50px;\
        padding:8px;">' + json.response + '</h4></center>'));
    };
