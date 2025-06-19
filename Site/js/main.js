$(function () {
  // Accordion
  $("#accordion").accordion({
    heightStyle: "content"
  });

  // Tabs
  $("#tabs").tabs();

  // Datepicker
  $("#datepicker").datepicker({
    showAnim: "slideDown"
  });

  // Tooltip
  $(document).tooltip();

  // Slider
  $("#slider").slider({
    value: 50,
    min: 0,
    max: 100,
    slide: function (event, ui) {
      $("#slider-label").text(ui.value);
    }
  });
});
