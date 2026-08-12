from retail_app.file_manager import clean_filename, save_order

def test_clean_filename_strips_unsafe_characters():
    assert clean_filename("../../etc/passwd") == "etcpasswd"

def test_clean_filename_keeps_safe_characters():
    assert clean_filename("bob_2") == "bob_2"

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

def test_save_order_cleans_traversal_attempt(tmp_path):
    save_order("../../etc/passwd", "pizza", orders_dir=tmp_path)
    assert (tmp_path / "etcpasswd.txt").exists()
