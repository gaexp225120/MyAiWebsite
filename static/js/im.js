            function showImg(thisimg) {
                var file = thisimg.files[0];
                if(window.FileReader) {
                    var fr = new FileReader();

                    var showimg = document.getElementById('sourceImage');
                    fr.onloadend = function(e) {
                        showimg.src = e.target.result;
                    };
                    fr.readAsDataURL(file);
                    showimg.style.display = 'block';
                }
            };
