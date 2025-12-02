def fifo_page_faults(pages, capacity):
    # 'frames' stores the current pages in memory
    frames = []
    page_faults = 0

    print(f"Reference String: {pages}")
    print(f"Frame Capacity: {capacity}")
    print("-" * 30)
    print(f"{'Page':<10} {'Frames':<15} {'Status'}")

    for page in pages:
        status = "Hit"
        
        if page not in frames:
            status = "Miss"
            page_faults += 1
            
            # If memory is full, remove the first element (FIFO)
            if len(frames) == capacity:
                frames.pop(0)
            
            frames.append(page)
        
        print(f"{page:<10} {str(frames):<15} {status}")

    print("-" * 30)
    print(f"Total Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example Reference String
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_slots = 4
    
    fifo_page_faults(reference_string, frame_slots)