$(document).ready(function () {
    // 載入城市資料
    $.ajax({
        url: '/api/cities/',
        type: 'GET',
        success: function(data) {
            let citySelect = $('#city');
            citySelect.empty();
            citySelect.append('<option value="">請選擇縣市</option>');
            
            $.each(data, function(id, name) {
                citySelect.append(`<option value="${id}">${name}</option>`);
            });
        },
        error: function(error) {
            console.error('載入城市資料失敗:', error);
        }
    });

    // 城市改變時載入鄉鎮資料
    $('#city').change(function() {
        let cityId = $(this).val();
        if (!cityId) return;
        
        $.ajax({
            url: `/api/towns/${cityId}/`,
            type: 'GET',
            success: function(data) {
                let townSelect = $('#town');
                townSelect.empty();
                townSelect.append('<option value="">請選擇鄉鎮</option>');
                
                $.each(data.towns, function(index, name) {
                    townSelect.append(`<option value="${name}">${name}</option>`);
                });
            },
            error: function(error) {
                console.error('載入鄉鎮資料失敗:', error);
            }
        });
    });

    // 添加生日年份選項
    let byear = document.getElementById("birthdate-year");
    let currentYear = new Date().getFullYear();
    
    // 添加空白選項
    let emptyOption = document.createElement("option");
    emptyOption.text = "請選擇年份";
    emptyOption.value = "";
    byear.add(emptyOption);
    
    for (let i = 0; i <= 30; i++) {
        let year = currentYear - i;
        let option = document.createElement("option");
        option.text = year;
        option.value = year;
        byear.add(option);
    }

    // 添加生日日期選項
    let bday = document.getElementById("birthdate-day");
    
    // 添加空白選項
    let emptyDayOption = document.createElement("option");
    emptyDayOption.text = "請選擇日期";
    emptyDayOption.value = "";
    bday.add(emptyDayOption);
    
    for (let i = 1; i <= 31; i++) {
        let day = i < 10 ? '0' + i : '' + i;
        let option = document.createElement("option");
        option.text = day;
        option.value = day;
        bday.add(option);
    }

    // 表單提交
    $('#submit-btn').click(function() {
        // 獲取CSRF令牌
        let csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        
        // 收集表單數據
        let formData = {
            name: $('#name').val(),
            student_id: $('#student-id').val(),
            birthdate_year: $('#birthdate-year').val(),
            birthdate_month: $('#birthdate-month').val(),
            birthdate_day: $('#birthdate-day').val(),
            birth_time: $('#birth-time').val(),
            city: $('#city').val(),
            town: $('#town').val(),
            goal: $('#goal').val()
        };
        
        // 提交資料
        $.ajax({
            url: '/api/submit/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                if (response.success) {
                    alert(response.message);
                    // 重置表單
                    $('#user-form')[0].reset();
                } else {
                    alert('提交失敗: ' + JSON.stringify(response.errors));
                }
            },
            error: function(error) {
                console.error('提交資料失敗:', error);
                alert('提交資料失敗');
            }
        });
    });

    // 添加清除按鈕的處理函數
    $('#clear-btn').click(function() {
        // 重置表單
        $('#user-form')[0].reset();
        clearErrors();
        
        // 重設預設城市為台北市
        $('#city').val('1').trigger('change');
    });
}); 