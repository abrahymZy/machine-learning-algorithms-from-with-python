def print_confusion_matrix(matrix, labels):
    """
    طباعة مصفوفة الارتباك كجدول منسق بدون مكتبات خارجية.
    
    :param matrix: مصفوفة ثنائية الأبعاد (قائمة قوائم أو numpy array)
    :param labels: قائمة بأسماء التصنيفات (نصوص)
    """
    n = len(labels)
    str_matrix = [[str(cell) for cell in row] for row in matrix]

    # حساب أقصى عرض لكل عمود لضمان محاذاة دقيقة
    row_label_width = max(len(str(lbl)) for lbl in labels)
    
    col_widths = []
    for j in range(n):
        max_col = len(str(labels[j]))
        for i in range(n):
            max_col = max(max_col, len(str_matrix[i][j]))
        col_widths.append(max_col + 4)  # إضافة مسافة هامشية للقراءة

    total_table_width = row_label_width + sum(col_widths) + (n + 1)

    # 2. ترويسة الأعمدة (أسماء الفئات)
    header_row = f"{'':>{row_label_width}} |"
    for j, lbl in enumerate(labels):
        header_row += f"{str(lbl):^{col_widths[j]}}|"
    print(header_row)

    # خط فاصل متناسق تماماً مع عرض التسميات
    separator = "-" * (row_label_width + 1) + "+" + "+".join("-" * w for w in col_widths) + "+"
    print(separator)

    # 3. طباعة الصفوف (التصنيف الفعلي + القيم)
    for i in range(n):
        row_str = f"{str(labels[i]):>{row_label_width}} |"
        for j in range(n):
            row_str += f"{str_matrix[i][j]:^{col_widths[j]}}|"
        print(row_str)
        print(separator)
