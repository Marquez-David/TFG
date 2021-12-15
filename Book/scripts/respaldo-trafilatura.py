postbody, len_text, sure_thing = extract_content(tree, ...)
# compare if necessary
if no_fallback is False:
    postbody, temp_text, len_text = compare_extraction(tree, ...)
    # add baseline as additional fallback
    if len(postbody) == 0:
        postbody, temp_text, len_text = baseline(filecontent)
# rescue: try to use original/dirty tree
elif sure_thing is False and len_text < MIN_EXTRACTED_SIZE:
    postbody, temp_text, len_text = baseline(filecontent)