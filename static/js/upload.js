var feedback = function(res) {
    if (res.success === true) {
        var get_link = res.data.link.replace(/^http:\/\//i, 'https://');
        document.querySelector('.status').innerHTML =
        'Url : ' + '<br><input class="image-url" value=\"' + get_link + '\"/>';
        document.querySelector('.urlarea').innerHTML =
        '<input class="image-url" value=\"' + get_link + '\"/>';
        document.getElementById('inputImage').value =imgtest ;
        document.getElementById('preimg').src =get_link ;
    }
};

new Imgur({
    clientid: '4409588f10776f7', //You can change this ClientID
    callback: feedback
});	