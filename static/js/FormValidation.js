function _createWarning(id, text) {
  let warning = document.createElement('p');
  warning.id = id;
  warning.className = 'warning';
  warning.innerHTML = text;
  return warning
}

function applyWarning(inputField, id, text) {
  $warning = $(`#${id}`);
  if (!$warning.length) {
      inputField.after(_createWarning(id, text));
      inputField[0].classList.add('inputWarning')
  }
}

function removeWarning(inputField) {
  $warning = $(`#${inputField[0].id}Warning`);
  if ($warning.length) {
      $warning.remove();
      inputField[0].classList.remove('inputWarning');
  }
}

function isFilled(inputField) {
  if (inputField.length) {
      $warning = $(`#${inputField[0].id}Warning`);
      if (!$warning.length) {
          if (inputField.val() === "") {
              applyWarning(inputField, `${inputField[0].id}Warning`, 'Input should not be blank')
              return false
          } else {
              removeWarning(inputField)
              return true
          }
      }
  }
}

function checkGrade($grade) {
    if ($grade.length) {
        let grade = parseFloat($grade.val())
        if (grade < 0 || grade > 100) {
            applyWarning($grade, `${$grade[0].id}Warning`, 'Grade should be between 0 and 100')
            return false
        } else {
            removeWarning($grade)
            return true
        }
    }
    return true
}

function checkPhone() {
    const $phone = $('#id_phone')
    if ($phone.length) {
        if (!$phone.val().startsWith('09')) {
            applyWarning($phone, `${$phone[0].id}Warning`, 'Phone number should begin with 09')
            return false
        } else if ($phone.val().length !== 10) {
            applyWarning($phone, `${$phone[0].id}Warning`, 'Phone number should be exactly 10 digits')
            return false
        } else {
            removeWarning($phone)
            return true
        }
    }
    return true
}

function submitForm(inputs) {
    gradePassList = []
    $('#id_chinese, #id_english, #id_math').each(function() {
        gradePassList.push(checkGrade($(this)))
    })

    result = inputs
        .map((input) => {
            return isFilled(input)
        })
        .filter((r) => {
            return r != undefined
        })
    
    if ((!result.includes(false)) && !gradePassList.includes(false) && checkPhone()) {
        $('#commonForm').submit();
    }        
}

$(document).ready(function() {
    const $inputs = [
        $('#id_firstName'), $('#id_lastName'), $('#id_phone'), $('#id_testNo'), $('#id_chinese'), $('#id_english'), 
        $('#id_math')
    ]

    $('#id_phone').on('blur', function() {
        checkPhone();
    })

    $('#id_chinese, #id_english, #id_math').each(function() {
        $(this).on('blur', function() {
            checkGrade($(this));
        });
    })

    $inputs.forEach(($input) => {
        $input.on('blur', function() {
            isFilled($input);
        })

        $input.on('input', function() {
            removeWarning($input);
        });
    });

    $('#submitBtn').on('click', function() {
        submitForm($inputs);
    })
});