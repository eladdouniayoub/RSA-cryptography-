var r_index = null;
var public_key2 = null;

$(document).ready(function() {
    $("#valid1").click(function() {
        $.ajax({
            url: '/valid1',
            method: 'POST',
            data: {
                txte: $('input[name="txt"]').val(),
                PnumA: $('input[name="Pnum"]').val(),
                Qnum: $('input[name="Qnum"]').val(),
            },
            success: function(response) {
                if (response.error) {
                    $('.r_number').empty();
                    $('.n_number').empty();
                    $('.set_prime').empty();
                    r_index = null;
                    alert(response.error);
                } else {
                    $('.r_number').html(response.R_index);
                    $('.n_number').html(response.N_number);
                    $('.set_prime').html(response.Set_prim.join(','));
                    r_index = response.R_index;
                }
            }
        });
    });
    $("#valid2").click(function() {
        $.ajax({
            url: '/valid2',
            method: 'POST',
            data: {
                PrimNbr: $('input[name="PrimNbr"]').val(),
                R_index: r_index
            },
            success: function(response) {
                if (response.error) {
                    $('.private_key2').empty();
                    alert(response.error);
                } else {
                    $('.private_key2').html(response.private_Key2);
                }
            }
        });
    });

    $("#chifrer").click(function() {
        $.ajax({
            url: '/chiffrer',
            method: 'POST',
            data: {
                txt: $('textarea[name="txt"]').val(),
                Public_key1: r_index,
                Public_key2: $('input[name="PrimNbr"]').val()
            },
            success: function(response) {
                if (response.error) {
                    $('textarea[name="texte"]').empty();
                    alert(response.error);
                } else {
                    $('textarea[name="texte"]').html(response.msgcrypte);
                }
            }
        });
    });

});