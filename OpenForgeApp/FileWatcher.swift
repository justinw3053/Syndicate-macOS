import Foundation

class FileWatcher {
    private var source: DispatchSourceFileSystemObject?
    private var fileDescriptor: Int32 = -1
    
    /// Starts watching a specific file path for write modifications.
    func startWatching(filePath: String, onChange: @escaping () -> Void) {
        stopWatching()
        
        // Open file using O_EVTONLY which doesn't prevent file-system unmounting/saving
        let fd = open(filePath, O_EVTONLY)
        guard fd >= 0 else { return }
        self.fileDescriptor = fd
        
        let queue = DispatchQueue.global(qos: .background)
        let source = DispatchSource.makeFileSystemObjectSource(
            fileDescriptor: fd,
            eventMask: .write,
            queue: queue
        )
        
        source.setEventHandler {
            onChange()
        }
        
        // Capture the file descriptor integer directly by value to avoid deinit weak-self bails
        source.setCancelHandler {
            close(fd)
        }
        
        self.source = source
        source.resume()
    }
    
    /// Stops and detaches the file-descriptor watcher.
    func stopWatching() {
        source?.cancel()
        source = nil
        fileDescriptor = -1
    }
    
    deinit {
        stopWatching()
    }
}
