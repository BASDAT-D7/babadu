from babadu_function.general import query_result

def role(member_id):
  result = query_result(f"SELECT * FROM umpire WHERE id='{member_id}';")
  if len(result) != 0:
    return "UMPIRE"
  result = query_result(f"SELECT * FROM pelatih WHERE id='{member_id}';")
  if len(result) != 0:
    return "PELATIH"
  result = query_result(f"SELECT * FROM atlet WHERE id='{member_id}';")
  if len(result) != 0:
    return "ATLET"
  return "NONE"