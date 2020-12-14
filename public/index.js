const fileInp = document.querySelector('.file');
const validFeedback = document.querySelector('.valid-feedback');
const invalidFeedback = document.querySelector('.invalid-feedback');


$(function () {
    $('.input-file-dummy').each(function () {
      $($(this).parent().find('.input-file-btn input')).on('change', {dummy: this}, function(ev) {
        $(ev.data.dummy)
          .val($(this).val().replace(/\\/g, '/').replace(/.*\//, ''))
          .trigger('focusout');
      });
      $(this).on('focusin', function () {
          $(this).attr('readonly', '');
        }).on('focusout', function () {
          $(this).removeAttr('readonly');
        }).on('click', function () {
          $(this).parent().find('.input-file-btn').click();
        });
    });
  });


const checkFile = (e) => {
    if (fileInp.files[0]) {
        validFeedback.style.display = 'block'
        invalidFeedback.style.display = 'none';
    }
    else {
        invalidFeedback.style.display = 'block';    
        validFeedback.style.display = 'none';
    }
};

fileInp.addEventListener('change', checkFile);