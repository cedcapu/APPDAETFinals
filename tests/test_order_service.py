from retail_app.order_service import sanitize_filename, save_order

def test_sanitize_filename_strips_unsafe_characters():
    assert sanitize_filename("../../etc/passwd") == "etcpasswd"

def test_sanitize_filename_keeps_safe_characters():
    assert sanitize_filename("bob_2") == "bob_2"

def test_save_order_rejects_empty_name(tmp_path):
    status = save_order("", "pizza", orders_dir=tmp_path)
    assert status == "Please enter a name."

def test_save_order_rejects_empty_order(tmp_path):
    status = save_order("bob", "", orders_dir=tmp_path)
    assert status == "Please enter an order."

def test_save_order_rejects_name_with_no_safe_characters(tmp_path):
    status = save_order("///", "pizza", orders_dir=tmp_path)
    assert status == "Name must contain letters, numbers, - or _."

def test_save_order_writes_file_and_returns_success(tmp_path):
    status = save_order("bob", "pizza", orders_dir=tmp_path)
    assert status == "Thanks for ordering!"
    assert (tmp_path / "bob.txt").read_text() == "pizza"

def test_save_order_sanitizes_traversal_attempt(tmp_path):
    save_order("../../etc/passwd", "pizza", orders_dir=tmp_path)
    # No file escapes tmp_path -- the sanitized name lands inside it.
    assert (tmp_path / "etcpasswd.txt").exists()
