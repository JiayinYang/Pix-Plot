'use strict';

var val_a;

$(function() {
  $('input, select').on('change', function(event) {
    var $element = $(event.target),
      $container = $element.closest('.example');

    if (!$element.data('tagsinput'))
      return;

    var val = $element.val();
    val_a = $element.tagsinput('items');
    numResult();

    if (val === null)
      val = "null";
    $('code', $('pre.val', $container)).html(($.isArray(val) ? JSON.stringify(val) : "\"" + val.replace('"', '\\"') + "\""));
    $('code', $('pre.items', $container)).html(JSON.stringify($element.tagsinput('items')));
  }).trigger('change');
});

function get(url, handleSuccess) {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == XMLHttpRequest.DONE) {
      if (xmlhttp.status === 200) {
        if (handleSuccess) handleSuccess(xmlhttp.responseText)
      } else {
        if (handleErr) handleErr(xmlhttp)
      }
    };
  };
  xmlhttp.open('GET', url, true);
  xmlhttp.send();
}

function numResult() {
  if (val_a.length != 0) {
    get('output/tags_data.json', function(data) {
      var data = JSON.parse(data);
      var clusters = [];
      for (var i = 0; i < val_a.length; i++) {
        clusters.push(data[val_a[i]].cluster);
      }
      var com_cluster = clusters.shift().filter(function(v) {
        return clusters.every(function(a) {
          return a.indexOf(v) !== -1;
        });
      });
      document.getElementById('totalNum').innerHTML = "Number of result: " + com_cluster.length;
    })
  }
  else {
    document.getElementById('totalNum').innerHTML = "Number of result: 0";
  }
}
