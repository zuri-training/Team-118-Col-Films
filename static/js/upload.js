const input = document.querySelector('#fileSelectorInput');
const preview = document.querySelector('.video-details');

input.style.opacity = 0;

input.addEventListener('change', updateVideoDisplay);


function updateVideoDisplay() {
    while(preview.firstChild) {
      preview.removeChild(preview.firstChild);
    }

    const curFiles = input.files;
    if (curFiles.length === 0) {
      let para = document.createElement('p');
      para.textContent = 'No files currently selected for upload';
      preview.appendChild(para);
    } else {
      const list = document.createElement('ol');
      preview.appendChild(list);

      for (const file of curFiles) {
        const listItem = document.createElement('li');
        const para = document.createElement('p');
        if (validFileType(file)) {
          let video = document.createElement('video');
          video.preload = 'metadata';
          video.id = 'tempVideo';
          video.controls = true;
          video.src = URL.createObjectURL(file);

          video.onloadedmetadata = function() {
            window.URL.revokeObjectURL(video.src);
          }
          video.src = URL.createObjectURL(file);

          para.innerHTML = `
            File name: <strong>${file.name}</strong>, File size: <strong>${returnFileSize(file.size)}</strong> and total Play Length of <strong><span id="v_length">${file.duration}</span></strong>.
          `;
          
          const subTitle = document.createElement('h2');
          subTitle.textContent = "Video preview"
          listItem.appendChild(subTitle)
          listItem.appendChild(video);
          listItem.appendChild(para);
        } else {
          para.textContent = `File name ${file.name}: Not a valid file type. Update your selection.`;
          para.classList.add("text-red")
          listItem.appendChild(para);
        }
        list.appendChild(listItem);
      }
    }
}


// https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
const fileTypes = [
    "video/mkv",
    "video/webm",
    "video/mp4",
    "video/m4p",
    "video/m4v",
    "video/3gp",
    "video/mpeg",
    "video/mpe",
    "video/mpeg",
    "video/mp2",
    "video/mpv",
    "video/mpeg4",
    "video/mov",
    "video/qt",
    "video/flv",
    "video/swf",
    "video/avchd",
    "video/avi",
    "video/wmv",
    "video/evo",
    "video/ogg",
];
  
function validFileType(file) {
    return fileTypes.includes(file.type);
}

function returnFileSize(number) {
    if (number < 1024) {
      return `${number} bytes`;
    } else if (number >= 1024 && number < 1048576) {
      return `${(number / 1024).toFixed(1)} KB`;
    } else if (number >= 1048576) {
      return `${(number / 1048576).toFixed(1)} MB`;
    }
}

var i = setInterval(function() {
    video = document.querySelector('#tempVideo');
    if(video.readyState > 0) {
        var durationsMinutes = parseInt(video.duration / 60, 10);
        var seconds = Number((video.duration % 60).toFixed(0));

        vid_len = document.querySelector('#v_length');
        vid_len.textContent = `${durationsMinutes}.${seconds} minutes`
        // clearInterval(i);
    };
    validateUpload(video)
}, 200);


function validateUpload(video) {
  minutes = parseInt(video.duration / 60, 10);
  seconds = Number((video.duration % 60).toFixed(0));
  length = parseFloat(`${minutes}.${seconds}`);
  if (length > 15.0) {
    button = document.querySelector("#uploadButton");
    button.disabled = "disabled";
    button.setAttribute("disabled", "disabled");
    button.setAttribute("title", "Video length larger than 15MB. Choose another video to upload!");
  } else {
    button.removeAttribute("title");
    button.removeAttribute("disabled");
  }
}