function setCookie(cname, cvalue, exdays) {
		    var d = new Date();
		    d.setTime(d.getTime() + (exdays*24*60*60*1000));
		    var expires = "expires="+d.toUTCString();
		    document.cookie = cname + "=" + cvalue + "; " + expires;
		}
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}
function checkCookie(question_id) {
    var user = getCookie("username");
    var question = getCookie("question_id");
    if (user != "" && question == question_id) {
        alert("Welcome again " + user + ".");
        document.getElementById('detailbody').innerHTML = 'You have already voted'
    } else {
        user = prompt("Please enter your name:", "");
        if (user != "" && user != null) {
            setCookie("username", user, 365);
            setCookie("question_id", question_id, 365);

        }
    }
}
function clicked() {
    checkConfirm = confirm('Do you want to Continue?');
    if (checkConfirm == true){
    	return true
    }
    else{
    	return false
    }
}