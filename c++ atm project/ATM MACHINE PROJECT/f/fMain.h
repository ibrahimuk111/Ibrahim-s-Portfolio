/***************************************************************
 * Name:      fMain.h
 * Purpose:   Defines Application Frame
 * Author:    ff ()
 * Created:   2025-03-04
 * Copyright: ff ()
 * License:
 **************************************************************/

#ifndef FMAIN_H
#define FMAIN_H

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "fApp.h"


#include <wx/button.h>
#include <wx/statline.h>
class fDialog: public wxDialog
{
    public:
        fDialog(wxDialog *dlg, const wxString& title);
        ~fDialog();

    protected:
        enum
        {
            idBtnQuit = 1000,
            idBtnAbout
        };
        wxStaticText* m_staticText1;
        wxButton* BtnAbout;
        wxStaticLine* m_staticline1;
        wxButton* BtnQuit;

    private:
        void OnClose(wxCloseEvent& event);
        void OnQuit(wxCommandEvent& event);
        void OnAbout(wxCommandEvent& event);
        DECLARE_EVENT_TABLE()
};

#endif // FMAIN_H
