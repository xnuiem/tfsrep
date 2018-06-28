(function() {
    function main() {
        var tabButtons = [].slice.call(document.querySelectorAll('ul.tab-nav li a.button'));

        tabButtons.map(function(button) {
            button.addEventListener('click', function() {
                document.querySelector('li a.active.button').classList.remove('active');
                button.classList.add('active');

                document.querySelector('.tab-pane.active').classList.remove('active');
                document.querySelector(button.getAttribute('href')).classList.add('active');
                chartArray = eval(button.getAttribute('href').substr(1));
                for (i = 0; i < chartArray.length; i++) {
                    Plotly.relayout(document.getElementById(chartArray[i]), { width: 450, height: 450, responsive: false })
                }

            })
        })
    }

    if (document.readyState !== 'loading') {
        main();
    } else {
        document.addEventListener('DOMContentLoaded', main);
    }
})();