let webcamStream = null;
let isWebcamActive = false;
let detectionInterval = null;

// Update analytics display
function updateAnalytics(results) {
    document.getElementById('studentCount').textContent = results.student_count;
    document.getElementById('behaviorCount').textContent = results.behaviors?.count || 0;
    document.getElementById('poseCount').textContent = results.poses?.pose_count || 0;
    document.getElementById('handRaisedCount').textContent = results.poses?.hand_raised_count || 0;
    
    // Show behavior breakdown
    const behaviorPanel = document.getElementById('behaviorPanel');
    const behaviorList = document.getElementById('behaviorList');
    
    if (results.behaviors?.breakdown && Object.keys(results.behaviors.breakdown).length > 0) {
        behaviorPanel.style.display = 'block';
        let html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 15px; margin-top: 15px;">';
        
        for (const [behavior, count] of Object.entries(results.behaviors.breakdown)) {
            html += `<div style="background: white; padding: 15px; border-radius: 8px; text-align: center; border: 2px solid #667eea;">
                <div style="font-size: 0.9em; color: #495057; margin-bottom: 5px;">${behavior}</div>
                <div style="font-size: 2em; font-weight: bold; color: #667eea;">${count}</div>
            </div>`;
        }
        
        html += '</div>';
        behaviorList.innerHTML = html;
    } else {
        behaviorPanel.style.display = 'none';
    }
}

// Detect from uploaded image
async function detectImage() {
    const fileInput = document.getElementById('imageUpload');
    if (!fileInput.files.length) {
        alert('⚠️ Please select an image first');
        return;
    }

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    try {
        const response = await fetch('/detect_image', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (data.success) {
            updateAnalytics(data.results);
            
            // Display uploaded image
            const reader = new FileReader();
            reader.onload = (e) => {
                document.getElementById('detectionResult').src = e.target.result;
            };
            reader.readAsDataURL(fileInput.files[0]);
            
            // Clean notification message
            let message = `✓ Detection Complete!\n\n`;
            message += `👥 Students Detected: ${data.results.student_count}\n`;
            message += `🎯 Behaviors Found: ${data.results.behaviors?.count || 0}\n`;
            message += `🤸 Poses Analyzed: ${data.results.poses?.pose_count || 0}\n`;
            message += `✋ Hands Raised: ${data.results.poses?.hand_raised_count || 0}\n`;
            
            if (data.results.behaviors?.breakdown) {
                message += `\n📊 Behavior Details:\n`;
                for (const [behavior, count] of Object.entries(data.results.behaviors.breakdown)) {
                    message += `   • ${behavior}: ${count}\n`;
                }
            }
            
            alert(message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('❌ Detection failed. Please try again.');
    }
}

// Toggle webcam on/off
async function toggleWebcam() {
    const btn = document.getElementById('webcamBtn');
    
    if (!isWebcamActive) {
        try {
            webcamStream = await navigator.mediaDevices.getUserMedia({ 
                video: { width: 640, height: 480 } 
            });
            
            const video = document.getElementById('webcam');
            video.srcObject = webcamStream;
            video.style.display = 'block';
            document.getElementById('detectionResult').style.display = 'none';
            
            isWebcamActive = true;
            btn.textContent = 'Stop Webcam';
            
            // Start detection loop
            detectionInterval = setInterval(detectWebcamFrame, 1000);
        } catch (error) {
            console.error('Webcam error:', error);
            alert('❌ Could not access webcam.\nPlease check camera permissions.');
        }
    } else {
        stopWebcam();
    }
}

function stopWebcam() {
    if (webcamStream) {
        webcamStream.getTracks().forEach(track => track.stop());
        document.getElementById('webcam').style.display = 'none';
        document.getElementById('detectionResult').style.display = 'block';
    }
    
    if (detectionInterval) {
        clearInterval(detectionInterval);
    }
    
    isWebcamActive = false;
    document.getElementById('webcamBtn').textContent = 'Start Webcam';
}

// Detect from webcam frame
async function detectWebcamFrame() {
    const video = document.getElementById('webcam');
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0, 0);
    
    const frameData = canvas.toDataURL('image/jpeg');
    
    try {
        const response = await fetch('/detect_webcam', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ frame: frameData })
        });
        
        const data = await response.json();
        if (data.success) {
            updateAnalytics(data.results);
            
            // Display annotated frame
            const resultImg = document.getElementById('detectionResult');
            resultImg.src = data.annotated_frame;
            resultImg.style.display = 'block';
            video.style.display = 'none';
            
            setTimeout(() => {
                if (isWebcamActive) {
                    video.style.display = 'block';
                    resultImg.style.display = 'none';
                }
            }, 800);
        }
    } catch (error) {
        console.error('Detection error:', error);
    }
}

// Save attendance manually
async function saveAttendance() {
    const studentCount = parseInt(document.getElementById('studentCount').textContent);
    
    if (studentCount === 0) {
        alert('⚠️ No students detected yet.\nPlease run detection first.');
        return;
    }
    
    try {
        const response = await fetch('/save_attendance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                student_count: studentCount
            })
        });
        
        const data = await response.json();
        if (data.success) {
            alert(`✓ Attendance Saved Successfully!\n\n${studentCount} students recorded.`);
            loadLogs();
        }
    } catch (error) {
        console.error('Error:', error);
        alert('❌ Failed to save attendance.\nPlease try again.');
    }
}

// Load today's logs
async function loadLogs() {
    try {
        const response = await fetch('/get_logs');
        const data = await response.json();
        
        const container = document.getElementById('logsContainer');
        
        if (data.logs.length === 0) {
            container.innerHTML = '<p>No logs for today yet.</p>';
            return;
        }
        
        let html = '<table><thead><tr><th>Time</th><th>Students Detected</th></tr></thead><tbody>';
        
        data.logs.forEach(log => {
            html += `<tr>
                <td>${log.Time}</td>
                <td><strong>${log['Student Count']}</strong></td>
            </tr>`;
        });
        
        html += '</tbody></table>';
        container.innerHTML = html;
    } catch (error) {
        console.error('Error loading logs:', error);
    }
}

// Load logs on page load
window.addEventListener('load', loadLogs);
