def optimal_page_replacement(data, num_frames):
    frames = [None] * num_frames  # Initialize a list to represent the frames in memory
    page_faults = 0  # Initialize the page fault counter

    for i, page in enumerate(data):
        if page not in frames:
            # If the page is not in the frames, it's a page fault
            page_faults += 1
            if None in frames:
                # If there are empty frames, simply put the page in an empty frame
                empty_frame_index = frames.index(None)
                frames[empty_frame_index] = page
            else:
                # If there are no empty frames, determine the page to replace based on future references
                future_references = [None] * num_frames  # Initialize a list to store future references
                for j in range(num_frames):
                    if frames[j] in data[i + 1:]:
                        future_references[j] = data[i + 1:].index(frames[j])
                    else:
                        future_references[j] = float('inf')  # Page not referenced again
                page_to_replace = frames[future_references.index(max(future_references))]
                frame_index_to_replace = frames.index(page_to_replace)
                frames[frame_index_to_replace] = page
    return page_faults

# Example usage:
data = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0]
num_frames = 4
faults = optimal_page_replacement(data, num_frames)
print("Page Faults (Optimal):", faults)
