from retail_app.file_manager import clean_filename, save_order

def test_clean_filename_cuts_invalid_characters():
    assert clean_filename("../../etc/passwd") == "etcpasswd"

def test_clean_filename_keeps_valid_characters():
    assert clean_filename("bob_2") == "bob_2"

def test_save_order_rejects_empty_name(tmp_path):
    status = save_order("", "pizza", orders_dir=tmp_path)
    assert status == "P"

def test_save_order_rejects_empty_order(tmp_path):
    status = save_order("bob", "", orders_dir=tmp_path)
    assert status == ""

def test_save_order_rejects_name_with_invalid_characters(tmp_path):
    status = save_order("///", "pizza", orders_dir=tmp_path)
    assert status == ""

def test_save_order_writes_file(tmp_path):
    status = save_order("bob", "pizza", orders_dir=tmp_path)
    assert status == ""
    assert (tmp_path / "bob.txt").read_text() == "pizza"