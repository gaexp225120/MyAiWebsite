var feedback = function(res) {
    if (res.success === true) {
        var get_link = res.data.link.replace(/^http:\/\//i, 'https://');
        document.querySelector('.status').classList.add('bg-success');
        document.querySelector('.status').innerHTML =
            'Url : ' + '<br><input class="image-url" value=\"' + get_link + '\"/>';
    }
};

new Imgur({
    clientid: '4409588f10776f7', //You can change this ClientID
    callback: feedback
});