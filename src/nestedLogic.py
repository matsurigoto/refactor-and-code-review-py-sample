def determine_access(user_role, has_permission, is_active):
    if user_role == "admin":
        if has_permission:
            if is_active:
                return "Active admin account with full access."
            else:
                return "Inactive admin account."
        else:
            return "Admin account lacks necessary permissions."
    else:
        return "Access denied."


# 測試函數
print(determine_access("admin", True, True))
print(determine_access("admin", True, False))
print(determine_access("admin", False, True))
print(determine_access("user", true, true))