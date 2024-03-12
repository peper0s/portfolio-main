<script>
if (window.location.hash!='') {
    window.hashName = window.location.hash;
    window.location.hash = '';
    $(document).ready(function() {
        $('html').animate({scrollTop: $(window.hashName).offset().top}, 2000, function() {
            window.location.hash = window.hashName;
        });
    });
}
</script>