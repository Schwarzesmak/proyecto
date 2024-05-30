
$(document).ready(function () {
    $('#addUserForm').submit(function (e) {
        e.preventDefault();
        let nombre = $('#nombre').val();
        let email = $('#email').val();
        let rowCount = $('#userTable tr').length;
        let newRow = '<tr><td>' + rowCount + '</td><td>' + nombre + '</td><td>' + email + '</td><td><button class="btn btn-sm btn-primary editBtn" data-user-id="' + rowCount + '">Editar</button><button class="btn btn-sm btn-danger deleteBtn">Eliminar</button></td></tr>';
        $('#userTable tbody').append(newRow);
        $('#addUserForm').trigger("reset");
    });

    $('#userTable').on('click', '.deleteBtn', function () {
        $(this).closest('tr').remove();
        $('#userTable tbody tr').each(function (index) {
            $(this).find('td:first').text(index + 1);
        });
    });
    $('#userTable').on('click', '.editBtn', function () {
        let row = $(this).closest('tr');
        let email = row.find('td:eq(2)').text();

        $('#editNombre').val(row.find('td:eq(1)').text());
        $('#editEmail').val(email);
        $('#editUserForm').show().data('user-email', email);
    });

    $('#editForm').submit(function (e) {
        e.preventDefault();
        let userEmail = $('#editUserForm').data('user-email');
        let nombre = $('#editNombre').val();
        let email = $('#editEmail').val();

        $('#userTable tbody tr').each(function () {
            if ($(this).find('td:eq(2)').text() === userEmail) {
                $(this).find('td:eq(1)').text(nombre);
                $(this).find('td:eq(2)').text(email);
                return false;
            }
        });

        $('#editUserForm').hide();
    });

    $('#userTable').on('click', '.deleteBtn', function () {
        $(this).closest('tr').remove();
        $('#userTable tbody tr').each(function (index) {
            $(this).find('td:first').text(index + 1);
        });
    });
});
