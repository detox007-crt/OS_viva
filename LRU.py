def lru_page_faults(pages, capacity):
    # 'frames' stores the current pages in memory
    # We use a list to represent the stack/queue:
    # Index 0 is Least Recently Used (LRU)
    # Last Index is Most Recently Used (MRU)
    frames = []
    page_faults = 0

    print(f"Reference String: {pages}")
    print(f"Frame Capacity: {capacity}")
    print("-" * 35)
    print(f"{'Page':<10} {'Frames':<15} {'Status'}")

    for page in pages:
        status = "Hit"
        
        if page not in frames:
            status = "Miss"
            page_faults += 1
            
            # If memory is full, remove the Least Recently Used (index 0)
            if len(frames) == capacity:
                frames.pop(0)
            
            # Add new page to the MRU position (end of list)
            frames.append(page)
            
        else:
            # Page exists (Hit). We must update its usage status.
            # Remove it from its current position and append to end (MRU)
            frames.remove(page)
            frames.append(page)
        
        print(f"{page:<10} {str(frames):<15} {status}")

    print("-" * 35)
    print(f"Total Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example Reference String
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_slots = 4
    
    lru_page_faults(reference_string, frame_slots)
