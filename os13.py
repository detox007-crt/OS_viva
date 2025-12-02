def optimal_page_faults(pages, capacity):
    frames = []
    page_faults = 0

    print(f"Reference String: {pages}")
    print(f"Frame Capacity: {capacity}")
    print("-" * 35)
    print(f"{'Page':<10} {'Frames':<15} {'Status'}")

    for i in range(len(pages)):
        page = pages[i]
        status = "Hit"
        
        if page not in frames:
            status = "Miss"
            page_faults += 1
            
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Optimal Replacement Logic:
                # Find the page in 'frames' that will not be used 
                # for the longest period of time in the future.
                
                furthest_index = -1
                page_to_replace = -1
                
                # Look ahead for each page currently in memory
                for f_page in frames:
                    try:
                        # Find the next occurrence of this page in the future list
                        # slices [i+1:] creates a sublist of future pages
                        next_use = pages[i+1:].index(f_page)
                    except ValueError:
                        # ValueError means page is not found in future -> Infinite distance
                        next_use = float('inf')
                    
                    if next_use > furthest_index:
                        furthest_index = next_use
                        page_to_replace = f_page
                
                # Replace the identified page
                frames[frames.index(page_to_replace)] = page
        
        print(f"{page:<10} {str(frames):<15} {status}")

    print("-" * 35)
    print(f"Total Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example Reference String
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_slots = 4
    
    optimal_page_faults(reference_string, frame_slots)