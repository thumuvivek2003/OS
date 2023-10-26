def fifo_page_replacement(data, num_frames):
    # Initialize a list to represent the frames in memory
    frames = [None] * num_frames
    page_faults = 0  # Initialize the page fault counter
    frame_index = 0  # Initialize the index for the current frame to replace

    for page in data:
        if page not in frames:
            # If the page is not in the frames, it's a page fault
            page_faults += 1
            frames[frame_index] = page  # Replace the page in the current frame
            frame_index = (frame_index + 1) % num_frames  # Update the frame index using FIFO

    return page_faults

# Example usage:
data = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0]
num_frames = 3
faults = fifo_page_replacement(data, num_frames)
print("Page Faults (FIFO):", faults)
